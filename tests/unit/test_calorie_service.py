
from app.application.services.calorie_service import estimate_session_calories

def test_svc():
    r = estimate_session_calories(weight_kg=80, duration_minutes=30, activity="strength")
    assert r["kcal"] > 0
