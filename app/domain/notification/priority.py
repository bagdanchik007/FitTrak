"""Notification priority ranking."""

ORDER = {"high": 0, "normal": 1, "low": 2}

def priority_rank(level: str | None) -> int:
    return ORDER.get((level or "normal").lower(), 1)
