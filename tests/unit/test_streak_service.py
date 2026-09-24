from datetime import date, timedelta

from app.application.services.streak_service import StreakService


def test_streak_service_summarize():
    today = date(2026, 10, 14)
    days = [today, today - timedelta(days=1)]
    result = StreakService().summarize(days, today=today)
    assert result["current_streak_days"] == 2
    assert result["total_workout_days"] == 2
    assert result["last_workout_date"] == today
