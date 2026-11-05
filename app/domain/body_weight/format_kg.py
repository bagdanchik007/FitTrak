"""Format kg values for display."""

def format_kg(value: float | None, *, digits: int = 1) -> str:
    if value is None:
        return "—"
    return f"{value:.{digits}f} kg"
