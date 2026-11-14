
from app.application.services.steps_service import steps_summary

def test_svc():
    r = steps_summary(steps=10000, height_cm=175, weight_kg=70)
    assert r["steps"] == 10000
    assert r["distance_km"] > 0
