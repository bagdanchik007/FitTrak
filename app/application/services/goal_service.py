"""Goal application service (thin wrapper for future domain logic)."""

from uuid import UUID, uuid4
from datetime import datetime, timezone

from app.domain.goal.entities import Goal
from app.schemas.goal import GoalCreate, GoalRead


def build_goal_entity(user_id: UUID, data: GoalCreate) -> Goal:
    now = datetime.now(timezone.utc)
    return Goal(
        id=uuid4(),
        user_id=user_id,
        title=data.title,
        description=data.description,
        target_value=data.target_value,
        current_value=data.current_value,
        unit=data.unit,
        deadline=data.deadline,
        is_completed=False,
        created_at=now,
        updated_at=now,
    )


def to_goal_read(goal: Goal) -> GoalRead:
    return GoalRead.model_validate(goal)
