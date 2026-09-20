from datetime import date, datetime, timezone
from uuid import uuid4

from app.domain.goal.entities import Goal
from app.domain.goal.services import is_goal_achieved, remaining_to_target


def _goal(**kwargs) -> Goal:
    now = datetime.now(timezone.utc)
    base = dict(
        id=uuid4(),
        user_id=uuid4(),
        title="Squat 140kg",
        description=None,
        target_value=140,
        current_value=120,
        unit="kg",
        deadline=date.today(),
        is_completed=False,
        created_at=now,
        updated_at=now,
    )
    base.update(kwargs)
    return Goal(**base)


def test_progress_ratio():
    g = _goal(current_value=70, target_value=140)
    assert g.progress_ratio == 0.5


def test_is_goal_achieved():
    assert is_goal_achieved(_goal(current_value=140, target_value=140)) is True
    assert is_goal_achieved(_goal(current_value=100, target_value=140)) is False


def test_remaining():
    assert remaining_to_target(_goal(current_value=100, target_value=140)) == 40
