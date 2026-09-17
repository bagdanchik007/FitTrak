import pytest

from app.domain.shared.value_objects import EmailAddress, Reps, WeightKg


def test_email_normalizes():
    email = EmailAddress("  Test@Example.COM ")
    assert str(email) == "test@example.com"


def test_email_invalid():
    with pytest.raises(ValueError):
        EmailAddress("not-an-email")


def test_weight_rejects_negative():
    with pytest.raises(ValueError):
        WeightKg(-1)


def test_reps_ok():
    assert Reps(10).value == 10
