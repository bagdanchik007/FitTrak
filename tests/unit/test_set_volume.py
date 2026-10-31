from app.domain.workout.set_volume import set_volume_kg

def test_volume():
    assert set_volume_kg(reps=10, weight_kg=50) == 500.0

def test_missing():
    assert set_volume_kg(reps=None, weight_kg=50) == 0.0
