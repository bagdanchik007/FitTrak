from datetime import date
from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.orm import selectinload

from app.core.dependencies import CurrentUserId, DbSession
from app.infrastructure.database.models.workout import WorkoutModel, WorkoutSetModel
from app.schemas.common import PaginatedResponse
from app.schemas.workout import WorkoutCreate, WorkoutRead, WorkoutUpdate

router = APIRouter(prefix="/workouts", tags=["Workouts"])

def _with_volume(workout) -> WorkoutRead:
    data = WorkoutRead.model_validate(workout)
    total = 0.0
    for s in data.sets:
        if s.weight_kg is not None and s.reps is not None:
            total += s.weight_kg * s.reps
    data.total_volume_kg = round(total, 2)
    return data




@router.post(
    "",
    response_model=WorkoutRead,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new workout with sets",
)
async def create_workout(
    data: WorkoutCreate,
    user_id: CurrentUserId,
    db: DbSession,
) -> WorkoutRead:
    workout = WorkoutModel(
        id=uuid4(),
        user_id=user_id,
        title=data.title,
        notes=data.notes,
        performed_at=data.performed_at,
        duration_minutes=data.duration_minutes,
    )
    db.add(workout)
    await db.flush()

    for set_data in data.sets:
        workout_set = WorkoutSetModel(
            id=uuid4(),
            workout_id=workout.id,
            exercise_id=set_data.exercise_id,
            set_number=set_data.set_number,
            reps=set_data.reps,
            weight_kg=set_data.weight_kg,
            rpe=set_data.rpe,
            notes=set_data.notes,
        )
        db.add(workout_set)

    await db.flush()
    await db.refresh(workout)

    # Reload with sets
    stmt = (
        select(WorkoutModel)
        .options(selectinload(WorkoutModel.sets))
        .where(WorkoutModel.id == workout.id)
    )
    result = await db.execute(stmt)
    workout = result.scalar_one()
    return _with_volume(workout)


@router.get(
    "",
    response_model=list[WorkoutRead],
    summary="List my workouts",
)
async def list_workouts(
    user_id: CurrentUserId,
    db: DbSession,
    skip: int = 0,
    limit: int = 20,
    search: str | None = None,
    from_date: date | None = None,
    to_date: date | None = None,
) -> list[WorkoutRead]:
    stmt = (
        select(WorkoutModel)
        .options(selectinload(WorkoutModel.sets))
        .where(
            WorkoutModel.user_id == user_id,
            WorkoutModel.deleted_at.is_(None),
        )
    )
    if search:
        stmt = stmt.where(WorkoutModel.title.ilike(f"%{search}%"))
    if from_date:
        stmt = stmt.where(WorkoutModel.performed_at >= from_date)
    if to_date:
        stmt = stmt.where(WorkoutModel.performed_at <= to_date)
    stmt = stmt.order_by(WorkoutModel.performed_at.desc()).offset(skip).limit(min(limit, 50))
    result = await db.execute(stmt)
    workouts = result.scalars().all()
    return [_with_volume(w) for w in workouts]


@router.get(
    "/{workout_id}",
    response_model=WorkoutRead,
    summary="Get a single workout",
)
async def get_workout(
    workout_id: UUID,
    user_id: CurrentUserId,
    db: DbSession,
) -> WorkoutRead:
    stmt = (
        select(WorkoutModel)
        .options(selectinload(WorkoutModel.sets))
        .where(
            WorkoutModel.id == workout_id,
            WorkoutModel.user_id == user_id,
            WorkoutModel.deleted_at.is_(None),
        )
    )
    result = await db.execute(stmt)
    workout = result.scalar_one_or_none()
    if not workout:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Workout not found")
    return _with_volume(workout)


@router.delete(
    "/{workout_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Soft-delete a workout",
)
async def delete_workout(
    workout_id: UUID,
    user_id: CurrentUserId,
    db: DbSession,
) -> None:
    from datetime import datetime, timezone
    stmt = select(WorkoutModel).where(
        WorkoutModel.id == workout_id,
        WorkoutModel.user_id == user_id,
        WorkoutModel.deleted_at.is_(None),
    )
    result = await db.execute(stmt)
    workout = result.scalar_one_or_none()
    if not workout:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Workout not found")
    workout.deleted_at = datetime.now(timezone.utc)
    await db.flush()


@router.patch(
    "/{workout_id}",
    response_model=WorkoutRead,
    summary="Update workout metadata",
)
async def update_workout(
    workout_id: UUID,
    data: WorkoutUpdate,
    user_id: CurrentUserId,
    db: DbSession,
) -> WorkoutRead:
    stmt = (
        select(WorkoutModel)
        .options(selectinload(WorkoutModel.sets))
        .where(
            WorkoutModel.id == workout_id,
            WorkoutModel.user_id == user_id,
            WorkoutModel.deleted_at.is_(None),
        )
    )
    result = await db.execute(stmt)
    workout = result.scalar_one_or_none()
    if not workout:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Workout not found")
    if data.title is not None:
        workout.title = data.title
    if data.notes is not None:
        workout.notes = data.notes
    if data.performed_at is not None:
        workout.performed_at = data.performed_at
    if data.duration_minutes is not None:
        workout.duration_minutes = data.duration_minutes
    await db.flush()
    await db.refresh(workout)
    return _with_volume(workout)


# Pagination uses skip/limit; total count can be added similarly to exercises
