from app.domain.search.normalize import normalize_query

def test_normalize():
    assert normalize_query("  Push  Day ") == "push day"
