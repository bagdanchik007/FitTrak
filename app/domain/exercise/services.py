"""Exercise catalog pure helpers."""


def normalize_exercise_name(name: str) -> str:
    return " ".join(name.strip().split())


def is_compound_hint(name: str) -> bool:
    keys = ("squat", "deadlift", "bench", "press", "row", "pull")
    lower = name.lower()
    return any(k in lower for k in keys)
