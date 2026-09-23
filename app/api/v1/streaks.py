"""Workout streak calculation for the current user."""

from datetime import date, timedelta

from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy import select

from app.core.dependencies import CurrentUserId, DbSession
from app.infrastructure.database.models.workout import WorkoutModel

router = APIRouter(prefix="/streaks", tags=["Streaks"])


class StreakResponse(BaseModel):
    current_streak_days: int
    longest_streak_days: int
    last_workout_date: date | None
    total_workout_days: int


@router.get("/me", response_model=StreakResponse)
async def get_my_streak(user_id: CurrentUserId, db: DbSession) -> StreakResponse:
    stmt = (
        select(WorkoutModel.performed_at)
        .where(WorkoutModel.user_id == user_id, WorkoutModel.deleted_at.is_(None))
        .distinct()
        .order_by(WorkoutModel.performed_at.desc())
    )
    days = [row[0] for row in (await db.execute(stmt)).all()]
    if not days:
        return StreakResponse(
            current_streak_days=0,
            longest_streak_days=0,
            last_workout_date=None,
            total_workout_days=0,
        )

    unique_days = sorted(set(days), reverse=True)
    current = 0
    cursor = date.today()
    # allow streak to continue if last workout was yesterday or today
    if unique_days[0] < cursor - timedelta(days=1):
        current = 0
    else:
        expected = unique_days[0]
        for d in unique_days:
            if d == expected:
                current += 1
                expected = d - timedelta(days=1)
            elif d < expected:
                break

    longest = 1
    run = 1
    asc = sorted(set(days))
    for i in range(1, len(asc)):
        if asc[i] == asc[i - 1] + timedelta(days=1):
            run += 1
            longest = max(longest, run)
        else:
            run = 1

    return StreakResponse(
        current_streak_days=current,
        longest_streak_days=max(longest, current),
        last_workout_date=unique_days[0],
        total_workout_days=len(unique_days),
    )

# StreakResponse shape also defined in app.schemas.streak
