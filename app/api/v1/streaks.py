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
