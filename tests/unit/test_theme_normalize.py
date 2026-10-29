from app.domain.preference.theme import normalize_theme

def test_theme():
    assert normalize_theme("DARK") == "dark"
    assert normalize_theme("nope") == "system"
