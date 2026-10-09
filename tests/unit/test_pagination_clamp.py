from app.core.pagination import clamp_limit, clamp_skip

def test_clamp_limit():
    assert clamp_limit(None) == 20
    assert clamp_limit(5) == 5
    assert clamp_limit(999) == 100

def test_clamp_skip():
    assert clamp_skip(-1) == 0
    assert clamp_skip(10) == 10
