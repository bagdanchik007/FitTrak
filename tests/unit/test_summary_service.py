from app.application.services.summary_service import build_weekly_totals
from app.domain.summary.services import SessionStats


def test_build_weekly_totals():
    result = build_weekly_totals(
        [SessionStats(sets=10, volume_kg=200, duration_minutes=40)],
        workout_count=2,
    )
    assert result["workouts"] == 2
    assert result["total_sets"] == 10
    assert result["avg_volume_per_workout"] == 100.0
