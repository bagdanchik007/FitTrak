"""Application wrapper for workout title rules."""

from app.domain.workout.title import normalize_workout_title

def prepare_title(raw: str) -> str:
    return normalize_workout_title(raw)
