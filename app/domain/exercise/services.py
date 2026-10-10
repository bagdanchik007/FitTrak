"""Exercise catalog pure helpers."""


def normalize_exercise_name(name: str) -> str:
    return " ".join(name.strip().split())


def is_compound_hint(name: str) -> bool:
    keys = ("squat", "deadlift", "bench", "press", "row", "pull")
    lower = name.lower()
    return any(k in lower for k in keys)


_MUSCLE_ALIASES = {
    "chest": "chest",
    "pectorals": "chest",
    "back": "back",
    "lats": "back",
    "legs": "legs",
    "quads": "legs",
    "shoulders": "shoulders",
    "delts": "shoulders",
    "arms": "arms",
    "biceps": "arms",
    "triceps": "arms",
    "core": "core",
    "abs": "core",
}


def normalize_muscle_group(value: str | None) -> str | None:
    if not value:
        return None
    key = value.strip().lower()
    return _MUSCLE_ALIASES.get(key, key)
