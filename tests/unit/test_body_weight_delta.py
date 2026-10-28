from app.domain.body_weight.delta import trend_direction, week_delta_kg

def test_delta():
    assert week_delta_kg(80.2, 80.0) == 0.2
    assert trend_direction(0.2) == "up"
