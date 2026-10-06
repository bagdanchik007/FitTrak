"""Workout streak calculation for the current user."""

from fastapi import APIRouter
from sqlalchemy import select

from app.application.services.streak_service import StreakService
from app.core.dependencies import CurrentUserId, DbSession
from app.infrastructure.database.models.workout import WorkoutModel
from app.schemas.streak import StreakResponse

router = APIRouter(prefix="/streaks", tags=["Streaks"])


@router.get("/me", response_model=StreakResponse)
async def get_my_streak(user_id: CurrentUserId, db: DbSession) -> StreakResponse:
    stmt = (
        select(WorkoutModel.performed_at)
        .where(WorkoutModel.user_id == user_id, WorkoutModel.deleted_at.is_(None))
        .distinct()
        .order_by(WorkoutModel.performed_at.desc())
    )
    days = [row[0] for row in (await db.execute(stmt)).all()]
    summary = StreakService().summarize(days)
    return StreakResponse(**summary)


@router.get("/me/recovery")
async def get_recovery(user_id: CurrentUserId, db: DbSession) -> dict:
    from datetime import date

    from app.application.services.recovery_service import recovery_snapshot

    stmt = (
        select(WorkoutModel.performed_at)
        .where(WorkoutModel.user_id == user_id, WorkoutModel.deleted_at.is_(None))
        .order_by(WorkoutModel.performed_at.desc())
        .limit(1)
    )
    row = (await db.execute(stmt)).first()
    last = row[0] if row else None
    return recovery_snapshot(last, date.today())


@router.get("/me/consistency")
async def get_consistency(user_id: CurrentUserId, db: DbSession, window_days: int = 28) -> dict:
    from datetime import date, timedelta

    from app.application.services.consistency_service import consistency_report

    window_days = max(7, min(window_days, 90))
    from_d = date.today() - timedelta(days=window_days - 1)
    stmt = (
        select(WorkoutModel.performed_at)
        .where(
            WorkoutModel.user_id == user_id,
            WorkoutModel.deleted_at.is_(None),
            WorkoutModel.performed_at >= from_d,
        )
        .distinct()
    )
    days = {row[0] for row in (await db.execute(stmt)).all()}
    return consistency_report(len(days), window_days)

