from app.domain.workout.services import estimate_1rm


def test_estimate_1rm_basic():
    assert estimate_1rm(100, 1) == 103.3
    assert estimate_1rm(80, 5) == 93.3


def test_estimate_1rm_invalid():
    assert estimate_1rm(0, 5) is None
    assert estimate_1rm(100, 0) is None
