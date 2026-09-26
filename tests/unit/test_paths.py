from app.core.paths import API_V1, DOCS, HEALTH


def test_paths():
    assert API_V1.startswith("/api")
    assert DOCS == "/docs"
    assert "health" in HEALTH
