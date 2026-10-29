"""Non-blocking password quality hints (not validation rules)."""

def password_hints(password: str) -> list[str]:
    hints: list[str] = []
    if len(password) < 12:
        hints.append("prefer_12_plus_chars")
    if password.lower() == password or password.upper() == password:
        hints.append("mix_case")
    if not any(c.isdigit() for c in password):
        hints.append("add_digit")
    return hints
