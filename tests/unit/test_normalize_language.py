from app.domain.preference.services import normalize_language


def test_normalize_language():
    assert normalize_language("DE") == "de"
    assert normalize_language("xx") == "en"
    assert normalize_language(None) == "en"
