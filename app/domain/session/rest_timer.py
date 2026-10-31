"""Suggested rest seconds between sets by intensity."""

def suggested_rest_seconds(*, rpe: float | None = None, is_compound: bool = True) -> int:
    if rpe is not None and rpe >= 9:
        return 180 if is_compound else 120
    if rpe is not None and rpe >= 7:
        return 120 if is_compound else 90
    return 90 if is_compound else 60
