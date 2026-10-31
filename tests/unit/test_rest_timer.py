from app.domain.session.rest_timer import suggested_rest_seconds

def test_hard():
    assert suggested_rest_seconds(rpe=9.5, is_compound=True) == 180

def test_easy():
    assert suggested_rest_seconds(rpe=5, is_compound=False) == 60
