"""Generic text truncation with ellipsis."""

def truncate(text: str | None, *, max_len: int = 80) -> str:
    value = (text or "").strip()
    if len(value) <= max_len:
        return value
    return value[: max_len - 1].rstrip() + "…"
