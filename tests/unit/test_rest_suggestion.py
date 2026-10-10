from app.domain.workout.services import suggested_rest_seconds
from app.application.services.rest_service import rest_suggestion

def test_suggested_rest_seconds():
    assert suggested_rest_seconds(reps=3, weight_kg=120) == 180
    assert suggested_rest_seconds(reps=12, weight_kg=40) == 60

def test_rest_suggestion_payload():
    s = rest_suggestion(5, 80)
    assert "suggested_rest_seconds" in s
