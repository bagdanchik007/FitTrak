"""Count unread notifications from a boolean flag list."""

def unread_count(flags: list[bool]) -> int:
    return sum(1 for f in flags if f)
