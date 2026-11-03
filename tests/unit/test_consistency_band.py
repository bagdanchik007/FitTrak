from app.domain.consistency.band import consistency_band

def test_excellent():
    assert consistency_band(90) == "excellent"
