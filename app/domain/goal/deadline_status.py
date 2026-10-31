"""Classify goal deadline urgency."""

from datetime import date

def deadline_status(deadline: date | None, *, today: date | None = None) -> str:
    if deadline is None:
        return "none"
    day = today or date.today()
    days = (deadline - day).days
    if days < 0:
        return "overdue"
    if days == 0:
        return "due_today"
    if days <= 7:
        return "due_soon"
    return "upcoming"
