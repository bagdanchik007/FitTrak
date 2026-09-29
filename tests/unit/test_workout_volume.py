from types import SimpleNamespace

from app.domain.workout.services import (
    assert_set_numbers_unique,
    calculate_session_volume,
    count_completed_sets,
    estimate_1rm,
)
import pytest


def test_session_volume():
    sets = [
        SimpleNamespace(weight_kg=50.0, reps=10),
        SimpleNamespace(weight_kg=60.0, reps=5),
    ]
    assert calculate_session_volume(sets) == 800.0


def test_count_completed_sets():
    sets = [
        SimpleNamespace(weight_kg=40.0, reps=8),
        SimpleNamespace(weight_kg=None, reps=None),
    ]
    assert count_completed_sets(sets) == 1


def test_unique_set_numbers():
    assert_set_numbers_unique([1, 2, 3])
    with pytest.raises(ValueError):
        assert_set_numbers_unique([1, 1, 2])


def test_epley():
    assert estimate_1rm(100, 10) == 133.3
