from app.core.validators import is_strong_password, normalize_email, slugify


def test_strong_password():
    assert is_strong_password("SecurePass123!") is True
    assert is_strong_password("short1A") is False
    assert is_strong_password("nodigitsHERE") is False
    assert is_strong_password("12345678") is False


def test_normalize_email():
    assert normalize_email("  Foo@Bar.COM ") == "foo@bar.com"


def test_slugify():
    assert slugify("Bench Press!") == "bench-press"
