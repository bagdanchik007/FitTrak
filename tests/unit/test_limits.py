from app.core.limits import DEFAULT_PAGE_SIZE, MAX_PAGE_SIZE, MAX_WORKOUT_DURATION_MINUTES


def test_limits():
    assert DEFAULT_PAGE_SIZE == 20
    assert MAX_PAGE_SIZE == 100
    assert MAX_WORKOUT_DURATION_MINUTES == 600
