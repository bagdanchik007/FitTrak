from datetime import date, datetime, timezone
from uuid import uuid4

from app.domain.goal.entities import Goal
from app.domain.goal.progress import is_overdue, percent_complete


def test_percent_complete():
    now = datetime.now(timezone.utc)
    g = Goal(
        id=uuid4(),
        user_id=uuid4(),
        title="t",
        description=None,
        target_value=100,
        current_value=25,
        unit="kg",
        deadline=None,
        is_completed=False,
        created_at=now,
        updated_at=now,
    )
    assert percent_complete(g) == 25.0


def test_is_overdue():
    now = datetime.now(timezone.utc)
    g = Goal(
        id=uuid4(),
        user_id=uuid4(),
        title="t",
        description=None,
        target_value=10,
        current_value=1,
        unit=None,
        deadline=date(2020, 1, 1),
        is_completed=False,
        created_at=now,
        updated_at=now,
    )
    assert is_overdue(g, date(2026, 1, 1)) is True
