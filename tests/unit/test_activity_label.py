from app.domain.activity.feed_label import activity_label

def test_workout_label():
    assert activity_label("workout") == "Logged a workout"

def test_body_weight_label():
    assert "weight" in activity_label("body_weight").lower()

def test_unknown():
    assert activity_label("nope") == "Activity"
