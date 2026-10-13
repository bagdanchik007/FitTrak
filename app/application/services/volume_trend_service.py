"""Compare recent volume to prior window."""


def volume_trend_pct(current: float, previous: float) -> float | None:
    if previous <= 0:
        return None if current <= 0 else 100.0
    return round((current - previous) / previous * 100, 1)


def trend_direction(pct: float | None) -> str:
    if pct is None:
        return "unknown"
    if pct > 5:
        return "up"
    if pct < -5:
        return "down"
    return "flat"
