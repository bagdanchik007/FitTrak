from datetime import date, datetime, timezone
from uuid import uuid4

from app.application.services.goal_progress_service import goal_status
from app.domain.goal.entities import Goal


def test_goal_status():
    now = datetime.now(timezone.utc)
    g = Goal(
        id=uuid4(),
        user_id=uuid4(),
        title="x",
        description=None,
        target_value=50,
        current_value=50,
        unit="kg",
        deadline=date(2030, 1, 1),
        is_completed=True,
        created_at=now,
        updated_at=now,
    )
    status = goal_status(g, today=date(2026, 1, 1))
    assert status["percent_complete"] == 100.0
    assert status["is_completed"] is True
    assert status["is_overdue"] is False
