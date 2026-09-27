"""Weekly training summary."""

from datetime import date, timedelta

from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.application.services.summary_service import build_weekly_totals
from app.core.dependencies import CurrentUserId, DbSession
from app.domain.summary.services import SessionStats
from app.infrastructure.database.models.workout import WorkoutModel
from app.schemas.summary import WeeklySummary

router = APIRouter(prefix="/summary", tags=["Summary"])


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
    parts: list[SessionStats] = []
    for w in workouts:
        sets = 0
        volume = 0.0
        for s in w.sets or []:
            sets += 1
            if s.weight_kg is not None and s.reps is not None:
                volume += s.weight_kg * s.reps
        parts.append(
            SessionStats(
                sets=sets,
                volume_kg=volume,
                duration_minutes=w.duration_minutes or 0,
            )
        )
    totals = build_weekly_totals(parts, workout_count=len(workouts))
    return WeeklySummary(
        from_date=from_d,
        to_date=to_d,
        workouts=totals["workouts"],
        total_sets=totals["total_sets"],
        total_volume_kg=totals["total_volume_kg"],
        total_duration_minutes=totals["total_duration_minutes"],
    )
