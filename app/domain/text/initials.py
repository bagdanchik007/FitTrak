"""Build initials from a display name."""

def initials(name: str | None, *, max_chars: int = 2) -> str:
    parts = [p for p in (name or "").split() if p]
    if not parts:
        return "?"
    chars = "".join(p[0].upper() for p in parts[:max_chars])
    return chars[:max_chars]
