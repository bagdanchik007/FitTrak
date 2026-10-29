"""Exercise name normalization."""

def normalize_exercise_name(name: str) -> str:
    cleaned = " ".join((name or "").split())
    return cleaned.title() if cleaned else "Exercise"
