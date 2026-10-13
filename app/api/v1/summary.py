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


@router.get("/weekly-goal")
async def weekly_goal_progress(user_id: CurrentUserId, db: DbSession) -> dict:
    from datetime import date, timedelta

    from sqlalchemy import func, select

    from app.application.services.weekly_goal_service import weekly_goal_status
from app.domain.summary.services import frequency_band
    from app.infrastructure.database.models.preference import UserPreferenceModel
    from app.infrastructure.database.models.workout import WorkoutModel

    to_d = date.today()
    from_d = to_d - timedelta(days=6)
    count_stmt = (
        select(func.count())
        .select_from(WorkoutModel)
        .where(
            WorkoutModel.user_id == user_id,
            WorkoutModel.deleted_at.is_(None),
            WorkoutModel.performed_at >= from_d,
            WorkoutModel.performed_at <= to_d,
        )
    )
    done = int((await db.execute(count_stmt)).scalar_one())
    pref_stmt = select(UserPreferenceModel).where(UserPreferenceModel.user_id == user_id)
    pref = (await db.execute(pref_stmt)).scalar_one_or_none()
    goal = pref.weekly_goal_workouts if pref else 3
    return weekly_goal_status(done, goal, from_date=from_d, to_date=to_d)


@router.get("/training-days")
async def training_days(user_id: CurrentUserId, db: DbSession, days: int = 7) -> dict:
    from datetime import date, timedelta

    from sqlalchemy import func

    days = max(1, min(days, 90))
    from_d = date.today() - timedelta(days=days - 1)
    stmt = select(func.count(func.distinct(WorkoutModel.performed_at))).where(
        WorkoutModel.user_id == user_id,
        WorkoutModel.deleted_at.is_(None),
        WorkoutModel.performed_at >= from_d,
    )
    # WorkoutModel may need import
    count = int((await db.execute(stmt)).scalar_one())
    return {
        "window_days": days,
        "training_days": count,
        "frequency_band": frequency_band(count, days),
    }


@router.get("/volume-trend")
async def volume_trend(user_id: CurrentUserId, db: DbSession) -> dict:
    """Compare last 7 days volume to the previous 7 days."""
    from datetime import date, timedelta

    from sqlalchemy import select

    from app.application.services.volume_trend_service import trend_direction, volume_trend_pct
    from app.infrastructure.database.models.workout import WorkoutModel, WorkoutSetModel

    today = date.today()
    cur_from = today - timedelta(days=6)
    prev_from = today - timedelta(days=13)
    prev_to = today - timedelta(days=7)

    async def window_volume(start, end) -> float:
        stmt = (
            select(WorkoutModel)
            .where(
                WorkoutModel.user_id == user_id,
                WorkoutModel.deleted_at.is_(None),
                WorkoutModel.performed_at >= start,
                WorkoutModel.performed_at <= end,
            )
        )
        workouts = (await db.execute(stmt)).scalars().all()
        total = 0.0
        for w in workouts:
            await db.refresh(w, attribute_names=["sets"]) if False else None
        # load sets via separate query for simplicity
        from sqlalchemy.orm import selectinload

        stmt2 = (
            select(WorkoutModel)
            .options(selectinload(WorkoutModel.sets))
            .where(
                WorkoutModel.user_id == user_id,
                WorkoutModel.deleted_at.is_(None),
                WorkoutModel.performed_at >= start,
                WorkoutModel.performed_at <= end,
            )
        )
        rows = (await db.execute(stmt2)).scalars().all()
        for w in rows:
            for s in w.sets or []:
                if s.weight_kg is not None and s.reps is not None:
                    total += float(s.weight_kg) * int(s.reps)
        return round(total, 2)

    current = await window_volume(cur_from, today)
    previous = await window_volume(prev_from, prev_to)
    pct = volume_trend_pct(current, previous)
    return {
        "current_7d_volume_kg": current,
        "previous_7d_volume_kg": previous,
        "change_pct": pct,
        "direction": trend_direction(pct),
    }

