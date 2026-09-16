from uuid import UUID, uuid4

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependencies import CurrentUserId, DbSession
from app.infrastructure.database.models.exercise import ExerciseModel
from app.schemas.common import PaginatedResponse
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
    response_model=PaginatedResponse[ExerciseRead],
    summary="List all exercises",
)
async def list_exercises(
    db: DbSession,
    skip: int = 0,
    limit: int = 50,
    muscle_group: str | None = None,
    search: str | None = None,
    equipment: str | None = None,
    sort_by: str = "name",
    order: str = "asc",
) -> PaginatedResponse[ExerciseRead]:
    stmt = (
        select(ExerciseModel)
        .where(ExerciseModel.deleted_at.is_(None))
        .offset(skip)
        .limit(min(limit, 100))
        .order_by(
            (ExerciseModel.created_at.desc() if order == "desc" else ExerciseModel.created_at.asc())
            if sort_by == "created_at"
            else (ExerciseModel.name.desc() if order == "desc" else ExerciseModel.name.asc())
        )
    )
    result = await db.execute(stmt)
    count_stmt = select(func.count()).select_from(
        select(ExerciseModel).where(ExerciseModel.deleted_at.is_(None)).subquery()
    )
    # recount with filters is approximate if we don't rebuild; simple total of page filter
    total_result = await db.execute(select(func.count()).select_from(ExerciseModel).where(ExerciseModel.deleted_at.is_(None)))
    total = total_result.scalar() or 0
    exercises = result.scalars().all()
    items = [ExerciseRead.model_validate(e) for e in exercises]
    return PaginatedResponse(items=items, total=total, skip=skip, limit=limit)


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
    from app.infrastructure.database.models.workout import WorkoutSetModel
    stmt = select(ExerciseModel).where(
        ExerciseModel.id == exercise_id,
        ExerciseModel.deleted_at.is_(None),
    )
    result = await db.execute(stmt)
    exercise = result.scalar_one_or_none()
    if not exercise:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Exercise not found")
    if exercise.created_by is not None and exercise.created_by != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    used = await db.execute(
        select(func.count()).select_from(WorkoutSetModel).where(WorkoutSetModel.exercise_id == exercise_id)
    )
    if (used.scalar() or 0) > 0:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Exercise is referenced in workout sets and cannot be deleted",
        )
    exercise.deleted_at = datetime.now(timezone.utc)
    await db.flush()


@router.patch(
    "/{exercise_id}",
    response_model=ExerciseRead,
    summary="Update an exercise",
)
async def update_exercise(
    exercise_id: UUID,
    data: ExerciseUpdate,
    user_id: CurrentUserId,
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
    if data.name is not None:
        exercise.name = data.name
    if data.description is not None:
        exercise.description = data.description
    if data.muscle_group is not None:
        exercise.muscle_group = data.muscle_group
    if data.equipment is not None:
        exercise.equipment = data.equipment
    await db.flush()
    await db.refresh(exercise)
    return ExerciseRead.model_validate(exercise)


# List endpoint returns PaginatedResponse with total count

# Future: POST /exercises/seed-defaults for system exercise catalog


DEFAULT_EXERCISES = [
    ("Bench Press", "chest", "barbell"),
    ("Squat", "legs", "barbell"),
    ("Deadlift", "back", "barbell"),
    ("Overhead Press", "shoulders", "barbell"),
    ("Barbell Row", "back", "barbell"),
    ("Pull-Up", "back", "bodyweight"),
    ("Dumbbell Curl", "biceps", "dumbbell"),
    ("Tricep Pushdown", "triceps", "cable"),
]


@router.post(
    "/seed-defaults",
    response_model=list[ExerciseRead],
    status_code=status.HTTP_201_CREATED,
    summary="Seed default system exercises for current user",
)
async def seed_defaults(
    user_id: CurrentUserId,
    db: DbSession,
) -> list[ExerciseRead]:
    created = []
    for name, muscle, equipment in DEFAULT_EXERCISES:
        existing = await db.execute(
            select(ExerciseModel).where(
                ExerciseModel.name == name,
                ExerciseModel.created_by == user_id,
                ExerciseModel.deleted_at.is_(None),
            )
        )
        if existing.scalar_one_or_none():
            continue
        ex = ExerciseModel(
            id=uuid4(),
            name=name,
            muscle_group=muscle,
            equipment=equipment,
            created_by=user_id,
        )
        db.add(ex)
        created.append(ex)
    await db.flush()
    for ex in created:
        await db.refresh(ex)
    return [ExerciseRead.model_validate(e) for e in created]

