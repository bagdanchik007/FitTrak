"""Body weight helpers."""

from app.domain.body_weight.entities import BodyWeightEntry


def delta_kg(entries: list[BodyWeightEntry]) -> float | None:
    """Difference between latest and oldest entry (positive = gain)."""
    if len(entries) < 2:
        return None
    ordered = sorted(entries, key=lambda e: e.recorded_at)
    return round(ordered[-1].weight_kg - ordered[0].weight_kg, 2)
