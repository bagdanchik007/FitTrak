from app.core.messages import EMAIL_TAKEN, USER_NOT_FOUND


def test_messages():
    assert "User" in USER_NOT_FOUND
    assert "email" in EMAIL_TAKEN.lower()
