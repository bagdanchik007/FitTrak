from app.core.pagination import PageParams, clamp_limit


def test_page_params_clamps_values():
    p = PageParams(skip=-5, limit=9999)
    assert p.skip == 0
    assert p.limit == 100


def test_clamp_limit():
    assert clamp_limit(0) == 20
    assert clamp_limit(50) == 50
    assert clamp_limit(500) == 100
