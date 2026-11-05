"""Minimum password length constant for forms."""

MIN_PASSWORD_LENGTH = 8

def meets_min_length(password: str) -> bool:
    return len(password or "") >= MIN_PASSWORD_LENGTH
