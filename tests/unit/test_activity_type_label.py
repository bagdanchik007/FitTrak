from app.domain.activity.services import activity_type_label

def test_activity_type_label():
    assert activity_type_label("workout") == "Workout"
    assert activity_type_label("body_weight") == "Body weight"
