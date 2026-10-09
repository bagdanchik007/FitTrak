"""Body-weight trend helpers (pure)."""


def trend_direction(delta_kg: float | None, threshold: float = 0.2) -> str:
    if delta_kg is None:
        return "unknown"
    if delta_kg > threshold:
        return "up"
    if delta_kg < -threshold:
        return "down"
    return "stable"


def moving_average(values: list[float], window: int = 3) -> float | None:
    if not values or window <= 0:
        return None
    sample = values[-window:]
    return round(sum(sample) / len(sample), 2)
