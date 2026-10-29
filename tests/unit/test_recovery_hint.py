from app.domain.recovery.suggestion import suggest_rest

def test_high():
    assert suggest_rest(trained_last_7_days=6)["rest_recommended"] is True
