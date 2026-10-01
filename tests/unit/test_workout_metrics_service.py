from types import SimpleNamespace

from app.application.services.workout_metrics_service import session_metrics
from app.domain.workout.services import sets_per_minute


def test_sets_per_minute():
    assert sets_per_minute(10, 20) == 0.5
    assert sets_per_minute(5, None) is None


def test_session_metrics():
    sets = [SimpleNamespace(weight_kg=50.0, reps=10)]
    m = session_metrics(sets, duration_minutes=25)
    assert m["total_volume_kg"] == 500.0
    assert m["completed_sets"] == 1
