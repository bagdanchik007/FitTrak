"""Normalize free-text search queries."""

def normalize_query(q: str | None) -> str:
    return " ".join((q or "").split()).lower()
