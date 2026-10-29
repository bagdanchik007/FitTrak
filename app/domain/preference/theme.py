"""Normalize UI theme preference values."""

ALLOWED = frozenset({"system", "light", "dark"})

def normalize_theme(value: str | None) -> str:
    v = (value or "system").strip().lower()
    return v if v in ALLOWED else "system"
