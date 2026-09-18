"""Domain helpers for exercises."""

from app.core.constants import EQUIPMENT_TYPES, MUSCLE_GROUPS


def is_known_muscle_group(value: str | None) -> bool:
    if value is None:
        return True
    return value.lower() in {m.lower() for m in MUSCLE_GROUPS}


def is_known_equipment(value: str | None) -> bool:
    if value is None:
        return True
    return value.lower() in {e.lower() for e in EQUIPMENT_TYPES}


def normalize_exercise_name(name: str) -> str:
    return " ".join(name.strip().split())
