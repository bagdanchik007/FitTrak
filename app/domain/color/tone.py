"""Map progress percent to a UI tone."""

def progress_tone(pct: float | None) -> str:
    if pct is None:
        return "muted"
    if pct >= 100:
        return "success"
    if pct >= 60:
        return "brand"
    return "muted"
