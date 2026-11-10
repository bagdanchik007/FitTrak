"""Percent of progress toward a target."""

def percent_of(*, current: float, target: float) -> float | None:
    if target <= 0:
        return None
    return round(min(100.0, max(0.0, (current / target) * 100)), 1)
