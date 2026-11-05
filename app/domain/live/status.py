"""Normalize live session connection status labels."""

def live_status_label(status: str | None) -> str:
    key = (status or "").lower()
    return {
        "connected": "Connected",
        "disconnected": "Disconnected",
        "reconnecting": "Reconnecting…",
        "error": "Connection error",
    }.get(key, "Unknown")
