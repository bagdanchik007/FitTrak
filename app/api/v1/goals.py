from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException, status
from sqlalchemy import select

from app.core.dependencies import CurrentUserId, DbSession
from app.infrastructure.database.models.goal import GoalModel
from app.schemas.goal import GoalCreate, GoalRead, GoalUpdate

router = APIRouter(prefix="/goals", tags=["Goals"])


@router.post("", response_model=GoalRead, status_code=status.HTTP_201_CREATED)
async def create_goal(data: GoalCreate, user_id: CurrentUserId, db: DbSession) -> GoalRead:
    goal = GoalModel(id=uuid4(), user_id=user_id, **data.model_dump())
    db.add(goal)
    await db.flush()
    await db.refresh(goal)
    return GoalRead.model_validate(goal)


@router.get("", response_model=list[GoalRead])
async def list_goals(user_id: CurrentUserId, db: DbSession) -> list[GoalRead]:
    stmt = (
        select(GoalModel)
        .where(GoalModel.user_id == user_id, GoalModel.deleted_at.is_(None))
        .order_by(GoalModel.created_at.desc())
    )
    result = await db.execute(stmt)
    return [GoalRead.model_validate(g) for g in result.scalars().all()]


@router.patch("/{goal_id}", response_model=GoalRead)
async def update_goal(
    goal_id: UUID, data: GoalUpdate, user_id: CurrentUserId, db: DbSession
) -> GoalRead:
    stmt = select(GoalModel).where(
        GoalModel.id == goal_id, GoalModel.user_id == user_id, GoalModel.deleted_at.is_(None)
    )
    goal = (await db.execute(stmt)).scalar_one_or_none()
    if not goal:
        raise HTTPException(status_code=404, detail="Goal not found")
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(goal, k, v)
    await db.flush()
    await db.refresh(goal)
    return GoalRead.model_validate(goal)


@router.delete("/{goal_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_goal(goal_id: UUID, user_id: CurrentUserId, db: DbSession) -> None:
    from datetime import datetime, timezone

    stmt = select(GoalModel).where(
        GoalModel.id == goal_id, GoalModel.user_id == user_id, GoalModel.deleted_at.is_(None)
    )
    goal = (await db.execute(stmt)).scalar_one_or_none()
    if not goal:
        raise HTTPException(status_code=404, detail="Goal not found")
    goal.deleted_at = datetime.now(timezone.utc)
    await db.flush()
