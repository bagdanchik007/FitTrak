from app.core.security import get_password_hash, verify_password


def test_wrong_password_returns_false():
    hashed = get_password_hash("CorrectHorseBattery1")
    assert verify_password("wrong-password-xx", hashed) is False


def test_long_password_hashes():
    pw = "Aa1" + ("x" * 100)
    hashed = get_password_hash(pw)
    assert verify_password(pw, hashed) is True
