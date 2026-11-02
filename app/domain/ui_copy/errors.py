"""User-facing error copy for common API failures."""

MESSAGES = {
    "unauthorized": "Please sign in again.",
    "not_found": "That item could not be found.",
    "validation": "Please check your input and try again.",
    "server": "Something went wrong. Try again shortly.",
}

def error_message(code: str | None) -> str:
    return MESSAGES.get((code or "").lower(), MESSAGES["server"])
