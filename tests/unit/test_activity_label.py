from app.domain.activity.feed_label import activity_label

def test_label():
    assert "workout" in activity_label("workout_created").lower()
