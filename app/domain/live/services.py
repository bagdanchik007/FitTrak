"""Live session pure helpers."""

ALLOWED_EVENTS = frozenset({"ping", "set_logged", "exercise_changed", "ended", "started"})


def normalize_live_event(event: str | None) -> str:
    if not event:
        return "ping"
    value = event.strip().lower()
    return value if value in ALLOWED_EVENTS else "ping"


def is_session_active(last_event: str | None) -> bool:
    return last_event not in (None, "ended")
