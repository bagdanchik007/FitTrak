from app.domain.exercise.services import is_compound_hint, normalize_exercise_name


def test_normalize_exercise_name():
    assert normalize_exercise_name("  bench   press ") == "bench press"


def test_is_compound_hint():
    assert is_compound_hint("Back Squat") is True
    assert is_compound_hint("Leg Extension") is False
