"""Shared validation helpers."""

import re

PASSWORD_MIN_LENGTH = 8


def password_has_digit(password: str) -> bool:
    return any(c.isdigit() for c in password)


def password_has_letter(password: str) -> bool:
    return any(c.isalpha() for c in password)


def is_strong_password(password: str) -> bool:
    return (
        len(password) >= PASSWORD_MIN_LENGTH
        and password_has_digit(password)
        and password_has_letter(password)
    )


def normalize_email(email: str) -> str:
    return email.strip().lower()


SLUG_RE = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    return SLUG_RE.sub("-", text.lower()).strip("-")
