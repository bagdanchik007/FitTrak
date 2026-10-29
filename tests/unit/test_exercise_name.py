from app.domain.exercise.name import normalize_exercise_name

def test_name():
    assert normalize_exercise_name("  bench press ") == "Bench Press"
