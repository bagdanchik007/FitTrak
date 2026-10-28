"""Streak milestone labels."""

MILESTONES = (3, 7, 14, 30, 60, 90, 180, 365)

def next_milestone(current: int) -> int | None:
    for m in MILESTONES:
        if current < m:
            return m
    return None

def milestone_reached(current: int) -> int | None:
    hit = [m for m in MILESTONES if m == current]
    return hit[0] if hit else None
