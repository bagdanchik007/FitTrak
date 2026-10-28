"""Sanitize user coach messages before processing."""

def sanitize_coach_message(message: str, *, max_len: int = 2000) -> str:
    text = " ".join((message or "").split())
    return text[:max_len]
