from app.domain.preference.services import normalize_theme

def test_normalize_theme():
    assert normalize_theme("Dark") == "dark"
    assert normalize_theme("nope") == "system"
