from app.domain.journal.services import is_allowed_mood, normalize_mood


def test_normalize_mood():
    assert normalize_mood("  Happy ") == "happy"
    assert normalize_mood(None) is None


def test_allowed_mood():
    assert is_allowed_mood("motivated") is True
    assert is_allowed_mood("unknown_mood_x") is False
