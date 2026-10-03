from app.application.services.weekly_goal_service import weekly_goal_status
from app.domain.summary.services import progress_toward_weekly_goal


def test_progress_toward_weekly_goal():
    assert progress_toward_weekly_goal(2, 4) == 0.5
    assert progress_toward_weekly_goal(5, 3) == 1.0


def test_weekly_goal_status_met():
    s = weekly_goal_status(3, 3)
    assert s["goal_met"] is True
    assert s["remaining"] == 0
