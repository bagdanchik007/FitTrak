"""Human-readable goal progress labels."""

def progress_label(current: float, target: float) -> str:
    if target <= 0:
        return "n/a"
    ratio = current / target
    if ratio >= 1:
        return "completed"
    if ratio >= 0.75:
        return "nearly_there"
    if ratio >= 0.4:
        return "on_track"
    return "getting_started"
