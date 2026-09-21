"""Weekly training summary."""

from datetime import date, timedelta

from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.core.dependencies import CurrentUserId, DbSession
from app.infrastructure.database.models.workout import WorkoutModel

router = APIRouter(prefix="/summary", tags=["Summary"])


class WeeklySummary(BaseModel):
    from_date: date
    to_date: date
    workouts: int
    total_sets: int
    total_volume_kg: float
    total_duration_minutes: int


@router.get("/weekly", response_model=WeeklySummary)
async def weekly_summary(user_id: CurrentUserId, db: DbSession) -> WeeklySummary:
    to_d = date.today()
    from_d = to_d - timedelta(days=6)
    stmt = (
        select(WorkoutModel)
        .options(selectinload(WorkoutModel.sets))
        .where(
            WorkoutModel.user_id == user_id,
            WorkoutModel.deleted_at.is_(None),
            WorkoutModel.performed_at >= from_d,
            WorkoutModel.performed_at <= to_d,
        )
    )
    workouts = (await db.execute(stmt)).scalars().all()
    total_sets = 0
    total_volume = 0.0
    total_duration = 0
    for w in workouts:
        total_duration += w.duration_minutes or 0
        for s in w.sets or []:
            total_sets += 1
            if s.weight_kg is not None and s.reps is not None:
                total_volume += s.weight_kg * s.reps
    return WeeklySummary(
        from_date=from_d,
        to_date=to_d,
        workouts=len(workouts),
        total_sets=total_sets,
        total_volume_kg=round(total_volume, 2),
        total_duration_minutes=total_duration,
    )
