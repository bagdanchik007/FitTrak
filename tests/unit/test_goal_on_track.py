from app.domain.goal.progress import is_on_track

def test_is_on_track():
    assert is_on_track(50, 5, 10) is True
    assert is_on_track(10, 9, 10) is False
