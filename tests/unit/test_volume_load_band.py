from app.domain.workout.services import average_working_weight, volume_load_band
from types import SimpleNamespace


def test_volume_load_band():
    assert volume_load_band(500) == "light"
    assert volume_load_band(3000) == "moderate"
    assert volume_load_band(8000) == "heavy"


def test_average_working_weight():
    sets = [
        SimpleNamespace(weight_kg=100.0, reps=5),
        SimpleNamespace(weight_kg=80.0, reps=8),
    ]
    assert average_working_weight(sets) == 90.0
