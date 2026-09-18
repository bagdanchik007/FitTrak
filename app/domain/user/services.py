"""User domain helpers."""

from app.core.validators import normalize_email


def normalize_user_email(email: str) -> str:
    return normalize_email(email)


def display_name(full_name: str | None, email: str) -> str:
    if full_name and full_name.strip():
        return full_name.strip()
    return email.split("@")[0]
