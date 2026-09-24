"""Pure calculations for weekly training summary."""

from dataclasses import dataclass


@dataclass(slots=True)
class SessionStats:
    sets: int = 0
    volume_kg: float = 0.0
    duration_minutes: int = 0


def merge_session_stats(parts: list[SessionStats]) -> SessionStats:
    total = SessionStats()
    for p in parts:
        total.sets += p.sets
        total.volume_kg += p.volume_kg
        total.duration_minutes += p.duration_minutes
    total.volume_kg = round(total.volume_kg, 2)
    return total


def average_volume_per_workout(total_volume: float, workouts: int) -> float:
    if workouts <= 0:
        return 0.0
    return round(total_volume / workouts, 2)
