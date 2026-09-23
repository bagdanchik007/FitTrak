"""Journal domain helpers."""

ALLOWED_MOODS = {"happy", "neutral", "tired", "motivated", "sore", "great"}


def normalize_mood(mood: str | None) -> str | None:
    if mood is None:
        return None
    value = mood.strip().lower()
    return value if value else None


def is_allowed_mood(mood: str | None) -> bool:
    if mood is None:
        return True
    return normalize_mood(mood) in ALLOWED_MOODS
