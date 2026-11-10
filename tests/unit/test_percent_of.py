from app.domain.math_util.percent import percent_of

def test_pct():
    assert percent_of(current=50, target=100) == 50.0
