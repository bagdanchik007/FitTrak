from app.domain.summary.services import frequency_band

def test_frequency_band():
    assert frequency_band(0, 7) == "none"
    assert frequency_band(1, 7) == "low"
    assert frequency_band(3, 7) == "moderate"
    assert frequency_band(5, 7) == "high"
