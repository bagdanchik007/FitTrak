from app.core.enums import ActivityType, Mood, WeightUnit


def test_enums():
    assert WeightUnit.KG == "kg"
    assert Mood.MOTIVATED == "motivated"
    assert ActivityType.WORKOUT == "workout"
