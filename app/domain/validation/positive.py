"""Basic positive number checks for form input."""

def is_positive_number(value: float | int | None) -> bool:
    return value is not None and value > 0
