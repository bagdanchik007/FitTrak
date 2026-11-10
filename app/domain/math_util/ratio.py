"""Simple ratio current/target."""

def ratio(current: float, target: float) -> float | None:
    if target == 0:
        return None
    return round(current / target, 3)
