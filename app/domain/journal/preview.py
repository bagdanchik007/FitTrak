"""Truncate journal notes for list cards."""

def journal_preview(notes: str | None, *, max_len: int = 160) -> str:
    text = (notes or "").strip()
    if len(text) <= max_len:
        return text or "—"
    return text[: max_len - 1].rstrip() + "…"
