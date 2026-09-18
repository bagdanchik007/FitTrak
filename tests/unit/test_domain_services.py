from uuid import uuid4

from app.domain.exercise.services import is_known_equipment, is_known_muscle_group, normalize_exercise_name
from app.domain.user.services import display_name, normalize_user_email
from app.domain.workout.entities import WorkoutSet
from app.domain.workout.services import calculate_session_volume, estimate_1rm


def test_normalize_exercise_name():
    assert normalize_exercise_name("  Bench   Press  ") == "Bench Press"


def test_known_muscle_and_equipment():
    assert is_known_muscle_group("chest") is True
    assert is_known_muscle_group("unknown_xyz") is False
    assert is_known_equipment("barbell") is True


def test_session_volume():
    sets = [
        WorkoutSet(id=uuid4(), workout_id=uuid4(), exercise_id=uuid4(), set_number=1, reps=10, weight_kg=50),
        WorkoutSet(id=uuid4(), workout_id=uuid4(), exercise_id=uuid4(), set_number=2, reps=5, weight_kg=60),
    ]
    assert calculate_session_volume(sets) == 800.0


def test_estimate_1rm():
    assert estimate_1rm(100, 10) == 133.3


def test_display_name():
    assert display_name("Ada", "ada@x.com") == "Ada"
    assert display_name(None, "bob@x.com") == "bob"
    assert normalize_user_email("  A@B.C  ") == "a@b.c"
