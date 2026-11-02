"""ISO week key helpers for grouping sessions."""

from datetime import date

def iso_week_key(d: date) -> str:
    y, w, _ = d.isocalendar()
    return f"{y}-W{w:02d}"
