from app.domain.stats_util.average import safe_average

def test_avg():
    assert safe_average([10, 20]) == 15.0
    assert safe_average([]) is None
