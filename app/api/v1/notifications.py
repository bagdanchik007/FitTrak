"""Derived in-app notifications from user training state."""

from datetime import date

from fastapi import APIRouter
from sqlalchemy import func, select

from app.core.dependencies import CurrentUserId, DbSession
from app.domain.notification.services import sort_notifications
from app.infrastructure.database.models.goal import GoalModel
from app.infrastructure.database.models.workout import WorkoutModel

router = APIRouter(prefix="/notifications", tags=["Notifications"])


@router.get("")
async def list_notifications(user_id: CurrentUserId, db: DbSession) -> list[dict]:
    items: list[dict] = []
    today = date.today()

    last_stmt = select(func.max(WorkoutModel.performed_at)).where(
        WorkoutModel.user_id == user_id,
        WorkoutModel.deleted_at.is_(None),
    )
    last = (await db.execute(last_stmt)).scalar_one_or_none()
    if last is None:
        items.append(
            {
                "kind": "tip",
                "title": "Log your first workout",
                "body": "Start tracking to unlock streaks and progress.",
                "created_at": today.isoformat(),
            }
        )
    elif (today - last).days >= 3:
        items.append(
            {
                "kind": "streak",
                "title": "Time to train",
                "body": f"It has been {(today - last).days} days since your last session.",
                "created_at": today.isoformat(),
            }
        )

    goal_stmt = select(GoalModel).where(
        GoalModel.user_id == user_id,
        GoalModel.deleted_at.is_(None),
        GoalModel.is_completed.is_(False),
        GoalModel.deadline.is_not(None),
        GoalModel.deadline < today,
    )
    overdue = (await db.execute(goal_stmt)).scalars().all()
    for g in overdue[:5]:
        items.append(
            {
                "kind": "goal",
                "title": "Goal overdue",
                "body": g.title,
                "created_at": today.isoformat(),
            }
        )

    return sort_notifications(items)
