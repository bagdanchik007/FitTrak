from app.domain.workout.services import density_band


def test_density_band():
    assert density_band(None) is None
    assert density_band(0.1) == "low"
    assert density_band(0.5) == "moderate"
    assert density_band(1.0) == "high"
