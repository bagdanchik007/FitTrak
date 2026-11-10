"""Format seconds as mm:ss."""

def format_mmss(total_seconds: int) -> str:
    s = max(0, int(total_seconds))
    m, sec = divmod(s, 60)
    return f"{m}:{sec:02d}"
