"""Pure domain rules for workout sessions (no I/O, no framework types)."""

from __future__ import annotations

from typing import Protocol


class SetLike(Protocol):
    weight_kg: float | None
    reps: int | None


def calculate_session_volume(sets: list[SetLike]) -> float:
    """Sum of weight_kg * reps across sets; missing values contribute 0."""
    total = 0.0
    for s in sets:
        if s.weight_kg is not None and s.reps is not None:
            total += float(s.weight_kg) * int(s.reps)
    return round(total, 2)


def count_completed_sets(sets: list[SetLike]) -> int:
    return sum(1 for s in sets if s.reps is not None and s.reps > 0)


def estimate_1rm(weight_kg: float, reps: int) -> float | None:
    """Epley estimate; undefined for non-positive inputs."""
    if reps <= 0 or weight_kg <= 0:
        return None
    return round(weight_kg * (1.0 + reps / 30.0), 1)


def assert_set_numbers_unique(set_numbers: list[int]) -> None:
    if len(set_numbers) != len(set(set_numbers)):
        raise ValueError("set_number values must be unique within a workout")


def sets_per_minute(set_count: int, duration_minutes: int | None) -> float | None:
    """Training density; None when duration is missing or non-positive."""
    if duration_minutes is None or duration_minutes <= 0 or set_count < 0:
        return None
    return round(set_count / duration_minutes, 2)
