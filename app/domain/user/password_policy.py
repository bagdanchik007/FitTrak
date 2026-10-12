"""Password policy helpers (pure)."""


def password_strength_score(password: str) -> int:
    """0–4 rough strength score."""
    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c.isupper() for c in password) and any(c.islower() for c in password):
        score += 1
    return score


def password_strength_label(score: int) -> str:
    return {0: "very_weak", 1: "weak", 2: "fair", 3: "good", 4: "strong"}.get(score, "weak")


def is_password_acceptable(password: str, minimum: int = 2) -> bool:
    return password_strength_score(password) >= minimum
