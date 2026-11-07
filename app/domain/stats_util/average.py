"""Safe average of numeric samples."""

def safe_average(values: list[float]) -> float | None:
    if not values:
        return None
    return round(sum(values) / len(values), 2)
