from app.application.services.volume_trend_service import trend_direction, volume_trend_pct

def test_volume_trend_pct():
    assert volume_trend_pct(110, 100) == 10.0
    assert volume_trend_pct(0, 0) is None

def test_trend_direction():
    assert trend_direction(10) == "up"
    assert trend_direction(-10) == "down"
    assert trend_direction(1) == "flat"
