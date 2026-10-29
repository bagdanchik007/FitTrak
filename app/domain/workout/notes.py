"""Truncate workout notes for list views."""

def truncate_notes(notes: str | None, *, max_len: int = 120) -> str:
    text = (notes or "").strip()
    if len(text) <= max_len:
        return text
    return text[: max_len - 1].rstrip() + "…"
