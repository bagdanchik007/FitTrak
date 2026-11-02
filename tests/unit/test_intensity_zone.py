from app.domain.intensity.zone import intensity_zone

def test_hard():
    assert intensity_zone(8) == "hard"

def test_easy():
    assert intensity_zone(3) == "easy"
