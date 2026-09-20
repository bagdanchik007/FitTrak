"""Simple activity feed based on recent workouts and body weight logs."""

from datetime import date

from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy import select

from app.core.dependencies import CurrentUserId, DbSession
from app.infrastructure.database.models.body_weight import BodyWeightModel
from app.infrastructure.database.models.workout import WorkoutModel

router = APIRouter(prefix="/activity", tags=["Activity"])


class ActivityItem(BaseModel):
    type: str
    title: str
    occurred_on: date
    meta: dict | None = None


@router.get("/feed", response_model=list[ActivityItem])
async def activity_feed(
    user_id: CurrentUserId, db: DbSession, limit: int = 20
) -> list[ActivityItem]:
    items: list[ActivityItem] = []

    w_stmt = (
        select(WorkoutModel)
        .where(WorkoutModel.user_id == user_id, WorkoutModel.deleted_at.is_(None))
        .order_by(WorkoutModel.performed_at.desc())
        .limit(limit)
    )
    for w in (await db.execute(w_stmt)).scalars().all():
        items.append(
            ActivityItem(
                type="workout",
                title=w.title,
                occurred_on=w.performed_at,
                meta={"duration_minutes": w.duration_minutes},
            )
        )

    b_stmt = (
        select(BodyWeightModel)
        .where(BodyWeightModel.user_id == user_id)
        .order_by(BodyWeightModel.recorded_at.desc())
        .limit(limit)
    )
    for b in (await db.execute(b_stmt)).scalars().all():
        items.append(
            ActivityItem(
                type="body_weight",
                title=f"Weight {b.weight_kg} kg",
                occurred_on=b.recorded_at,
                meta={"weight_kg": b.weight_kg},
            )
        )

    items.sort(key=lambda x: x.occurred_on, reverse=True)
    return items[:limit]
