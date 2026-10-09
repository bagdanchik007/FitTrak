from app.domain.body_weight.services import moving_average

def test_moving_average():
    assert moving_average([80, 81, 82], 3) == 81.0
    assert moving_average([], 3) is None
