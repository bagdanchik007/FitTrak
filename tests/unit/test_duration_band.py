from app.domain.workout.services import duration_band

def test_duration_band():
    assert duration_band(None) is None
    assert duration_band(20) == "short"
    assert duration_band(45) == "standard"
    assert duration_band(75) == "long"
    assert duration_band(100) == "extended"
