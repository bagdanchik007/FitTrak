from app.domain.user.password_policy import (
    is_password_acceptable,
    password_strength_label,
    password_strength_score,
)

def test_password_strength():
    assert password_strength_score("x") < password_strength_score("Abcdef12!")
    assert password_strength_label(4) == "strong"
    assert is_password_acceptable("short") is False
