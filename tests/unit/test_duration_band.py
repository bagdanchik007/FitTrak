from app.domain.workout.duration_band import duration_band

def test_bands():
    assert duration_band(20) == "short"
    assert duration_band(45) == "standard"
