
from app.domain.nutrition.calories import calories_burned

def test_burn():
    kcal = calories_burned(weight_kg=70, duration_minutes=60, activity="walking")
    assert kcal > 0
