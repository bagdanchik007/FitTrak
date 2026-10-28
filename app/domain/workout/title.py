"""Workout title normalization."""

def normalize_workout_title(title: str) -> str:
    cleaned = " ".join((title or "").split())
    return cleaned[:150] if cleaned else "Untitled workout"
