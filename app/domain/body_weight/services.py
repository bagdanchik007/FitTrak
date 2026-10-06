"""Body-weight trend helpers (pure)."""


def trend_direction(delta_kg: float | None, threshold: float = 0.2) -> str:
    if delta_kg is None:
        return "unknown"
    if delta_kg > threshold:
        return "up"
    if delta_kg < -threshold:
        return "down"
    return "stable"
