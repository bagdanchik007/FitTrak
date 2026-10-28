"""Classify workout duration for UI badges."""

def duration_band(minutes: int | None) -> str:
    if minutes is None or minutes < 0:
        return "unknown"
    if minutes < 30:
        return "short"
    if minutes < 60:
        return "standard"
    if minutes < 90:
        return "long"
    return "extended"
