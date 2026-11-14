
from app.domain.exercise.calorie_hint import activity_key_from_exercise

def test_hint():
    assert activity_key_from_exercise(name="Easy Run") == "running"
    assert activity_key_from_exercise(name="Bench Press") == "strength"
