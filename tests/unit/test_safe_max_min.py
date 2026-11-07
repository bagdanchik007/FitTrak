from app.domain.stats_util.max_min import safe_max, safe_min

def test_mm():
    assert safe_max([1, 5, 3]) == 5
    assert safe_min([1, 5, 3]) == 1
