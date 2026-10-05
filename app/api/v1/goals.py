from datetime import UTC, date, datetime
from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select

from app.core.dependencies import CurrentUserId, DbSession
from app.core.messages import GOAL_NOT_FOUND
from app.domain.goal.entities import Goal
from app.domain.goal.progress import is_overdue, percent_complete
from app.infrastructure.database.models.goal import GoalModel
from app.schemas.goal import GoalCreate, GoalRead, GoalUpdate

router = APIRouter(prefix="/goals", tags=["Goals"])


class GoalProgressRead(BaseModel):
    goal_id: UUID
    percent_complete: float | None
    is_overdue: bool
    is_completed: bool


def _to_domain(model: GoalModel) -> Goal:
    return Goal(
        id=model.id,
        user_id=model.user_id,
        title=model.title,
        description=model.description,
        target_value=model.target_value,
        current_value=model.current_value,
        unit=model.unit,
        deadline=model.deadline,
        is_completed=model.is_completed,
        created_at=model.created_at,
        updated_at=model.updated_at,
        deleted_at=model.deleted_at,
    )


@router.post("", response_model=GoalRead, status_code=status.HTTP_201_CREATED)
async def create_goal(data: GoalCreate, user_id: CurrentUserId, db: DbSession) -> GoalRead:
    goal = GoalModel(id=uuid4(), user_id=user_id, **data.model_dump())
    db.add(goal)
    await db.flush()
    await db.refresh(goal)
    return GoalRead.model_validate(goal)


@router.get("", response_model=list[GoalRead])
async def list_goals(
    user_id: CurrentUserId,
    db: DbSession,
    completed: bool | None = None,
    skip: int = 0,
    limit: int = 50,
) -> list[GoalRead]:
    stmt = select(GoalModel).where(GoalModel.user_id == user_id, GoalModel.deleted_at.is_(None))
    if completed is not None:
        stmt = stmt.where(GoalModel.is_completed == completed)
    stmt = stmt.order_by(GoalModel.created_at.desc()).offset(skip).limit(min(limit, 100))
    result = await db.execute(stmt)
    return [GoalRead.model_validate(g) for g in result.scalars().all()]


@router.get("/{goal_id}/progress", response_model=GoalProgressRead)
async def get_goal_progress(
    goal_id: UUID, user_id: CurrentUserId, db: DbSession
) -> GoalProgressRead:
    stmt = select(GoalModel).where(
        GoalModel.id == goal_id,
        GoalModel.user_id == user_id,
        GoalModel.deleted_at.is_(None),
    )
    goal = (await db.execute(stmt)).scalar_one_or_none()
    if not goal:
        raise HTTPException(status_code=404, detail=GOAL_NOT_FOUND)
    domain = _to_domain(goal)
    return GoalProgressRead(
        goal_id=goal.id,
        percent_complete=percent_complete(domain),
        is_overdue=is_overdue(domain, date.today()),
        is_completed=goal.is_completed,
    )


@router.patch("/{goal_id}", response_model=GoalRead)
async def update_goal(
    goal_id: UUID, data: GoalUpdate, user_id: CurrentUserId, db: DbSession
) -> GoalRead:
    stmt = select(GoalModel).where(
        GoalModel.id == goal_id, GoalModel.user_id == user_id, GoalModel.deleted_at.is_(None)
    )
    goal = (await db.execute(stmt)).scalar_one_or_none()
    if not goal:
        raise HTTPException(status_code=404, detail=GOAL_NOT_FOUND)
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(goal, k, v)
    # auto-complete when current reaches target
    if (
        goal.target_value is not None
        and goal.current_value is not None
        and goal.current_value >= goal.target_value
    ):
        goal.is_completed = True
    await db.flush()
    await db.refresh(goal)
    return GoalRead.model_validate(goal)


@router.delete("/{goal_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_goal(goal_id: UUID, user_id: CurrentUserId, db: DbSession) -> None:
    stmt = select(GoalModel).where(
        GoalModel.id == goal_id, GoalModel.user_id == user_id, GoalModel.deleted_at.is_(None)
    )
    goal = (await db.execute(stmt)).scalar_one_or_none()
    if not goal:
        raise HTTPException(status_code=404, detail=GOAL_NOT_FOUND)
    goal.deleted_at = datetime.now(UTC)
    await db.flush()


@router.post("/{goal_id}/complete", response_model=GoalRead)
async def complete_goal(goal_id: UUID, user_id: CurrentUserId, db: DbSession) -> GoalRead:
    stmt = select(GoalModel).where(
        GoalModel.id == goal_id, GoalModel.user_id == user_id, GoalModel.deleted_at.is_(None)
    )
    goal = (await db.execute(stmt)).scalar_one_or_none()
    if not goal:
        raise HTTPException(status_code=404, detail=GOAL_NOT_FOUND)
    goal.is_completed = True
    if goal.target_value is not None and goal.current_value is None:
        goal.current_value = goal.target_value
    elif goal.target_value is not None and goal.current_value is not None:
        goal.current_value = max(goal.current_value, goal.target_value)
    await db.flush()
    await db.refresh(goal)
    return GoalRead.model_validate(goal)


@router.post("/{goal_id}/reopen", response_model=GoalRead)
async def reopen_goal(goal_id: UUID, user_id: CurrentUserId, db: DbSession) -> GoalRead:
    stmt = select(GoalModel).where(
        GoalModel.id == goal_id, GoalModel.user_id == user_id, GoalModel.deleted_at.is_(None)
    )
    goal = (await db.execute(stmt)).scalar_one_or_none()
    if not goal:
        raise HTTPException(status_code=404, detail=GOAL_NOT_FOUND)
    goal.is_completed = False
    await db.flush()
    await db.refresh(goal)
    return GoalRead.model_validate(goal)


@router.get("/active-count")
async def active_goals_count(user_id: CurrentUserId, db: DbSession) -> dict[str, int]:
    from sqlalchemy import func

    stmt = (
        select(func.count())
        .select_from(GoalModel)
        .where(
            GoalModel.user_id == user_id,
            GoalModel.deleted_at.is_(None),
            GoalModel.is_completed.is_(False),
        )
    )
    total = (await db.execute(stmt)).scalar_one()
    return {"active_goals": int(total)}


@router.get("/with-progress")
async def list_goals_with_progress(
    user_id: CurrentUserId, db: DbSession, completed: bool | None = None
) -> list[dict]:
    from datetime import date

    from app.domain.goal.entities import Goal
    from app.domain.goal.progress import is_overdue, percent_complete

    stmt = select(GoalModel).where(GoalModel.user_id == user_id, GoalModel.deleted_at.is_(None))
    if completed is not None:
        stmt = stmt.where(GoalModel.is_completed == completed)
    stmt = stmt.order_by(GoalModel.created_at.desc())
    rows = (await db.execute(stmt)).scalars().all()
    out = []
    for g in rows:
        domain = Goal(
            id=g.id,
            user_id=g.user_id,
            title=g.title,
            description=g.description,
            target_value=g.target_value,
            current_value=g.current_value,
            unit=g.unit,
            deadline=g.deadline,
            is_completed=g.is_completed,
            created_at=g.created_at,
            updated_at=g.updated_at,
            deleted_at=g.deleted_at,
        )
        out.append(
            {
                **GoalRead.model_validate(g).model_dump(mode="json"),
                "percent_complete": percent_complete(domain),
                "is_overdue": is_overdue(domain, date.today()),
            }
        )
    return out
