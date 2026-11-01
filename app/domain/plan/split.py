"""Simple weekly training split rotation."""

SPLITS = ("push", "pull", "legs", "upper", "lower")

def next_split_day(last_focus: str | None, *, day_index: int = 0) -> str:
    if last_focus and last_focus.lower() in SPLITS:
        i = SPLITS.index(last_focus.lower())
        return SPLITS[(i + 1) % len(SPLITS)]
    return SPLITS[day_index % len(SPLITS)]
