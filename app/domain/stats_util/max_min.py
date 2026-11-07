"""Max/min helpers that tolerate empty lists."""

def safe_max(values: list[float]) -> float | None:
    return max(values) if values else None

def safe_min(values: list[float]) -> float | None:
    return min(values) if values else None
