from app.domain.progress.weekly_delta import volume_delta_pct

def test_up():
    assert volume_delta_pct(110, 100) == 10.0

def test_zero_prev():
    assert volume_delta_pct(50, 0) == 100.0
