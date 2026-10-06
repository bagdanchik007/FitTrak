from app.domain.body_weight.services import trend_direction


def test_trend_direction():
    assert trend_direction(1.0) == "up"
    assert trend_direction(-1.0) == "down"
    assert trend_direction(0.0) == "stable"
    assert trend_direction(None) == "unknown"
