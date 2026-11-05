"""Whether a goal is complete based on current vs target."""

def is_goal_complete(*, current: float | None, target: float | None) -> bool:
    if current is None or target is None or target <= 0:
        return False
    return current >= target
