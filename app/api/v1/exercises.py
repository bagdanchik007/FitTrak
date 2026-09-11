from uuid import UUID, uuid4

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependencies import CurrentUserId, DbSession
from app.infrastructure.database.models.exercise import ExerciseModel
from app.schemas.exercise import ExerciseCreate, ExerciseRead, ExerciseUpdate

router = APIRouter(prefix="/exercises", tags=["Exercises"])


@router.post(
    "",
    response_model=ExerciseRead,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new exercise",
)
async def create_exercise(
    data: ExerciseCreate,
    user_id: CurrentUserId,
    db: DbSession,
) -> ExerciseRead:
    exercise = ExerciseModel(
        id=uuid4(),
        name=data.name,
        description=data.description,
        muscle_group=data.muscle_group,
        equipment=data.equipment,
        created_by=user_id,
    )
    db.add(exercise)
    await db.flush()
    await db.refresh(exercise)
    return ExerciseRead.model_validate(exercise)


@router.get(
    "",
    response_model=list[ExerciseRead],
    summary="List all exercises",
)
async def list_exercises(
    db: DbSession,
    skip: int = 0,
    limit: int = 50,
    muscle_group: str | None = None,
) -> list[ExerciseRead]:
    stmt = (
        select(ExerciseModel)
        .where(ExerciseModel.deleted_at.is_(None))
        .offset(skip)
        .limit(min(limit, 100))
        .order_by(ExerciseModel.name)
    )
    result = await db.execute(stmt)
    exercises = result.scalars().all()
    return [ExerciseRead.model_validate(e) for e in exercises]


@router.get(
    "/{exercise_id}",
    response_model=ExerciseRead,
    summary="Get a single exercise",
)
async def get_exercise(
    exercise_id: UUID,
    db: DbSession,
) -> ExerciseRead:
    stmt = select(ExerciseModel).where(
        ExerciseModel.id == exercise_id,
        ExerciseModel.deleted_at.is_(None),
    )
    result = await db.execute(stmt)
    exercise = result.scalar_one_or_none()
    if not exercise:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Exercise not found")
    return ExerciseRead.model_validate(exercise)

# TODO: add DELETE /exercises/{id} using ExerciseService.delete

@router.delete(
    "/{exercise_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Soft-delete an exercise",
)
async def delete_exercise(
    exercise_id: UUID,
    user_id: CurrentUserId,
    db: DbSession,
) -> None:
    from datetime import datetime, timezone
    stmt = select(ExerciseModel).where(
        ExerciseModel.id == exercise_id,
        ExerciseModel.deleted_at.is_(None),
    )
    result = await db.execute(stmt)
    exercise = result.scalar_one_or_none()
    if not exercise:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Exercise not found")
    exercise.deleted_at = datetime.now(timezone.utc)
    await db.flush()

