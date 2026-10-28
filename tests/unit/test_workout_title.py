from app.domain.workout.title import normalize_workout_title

def test_normalize():
    assert normalize_workout_title("  Push   Day  ") == "Push Day"
