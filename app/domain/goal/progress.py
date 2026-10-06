"""Goal progress helpers."""

from app.domain.goal.entities import Goal


def percent_complete(goal: Goal) -> float | None:
    ratio = goal.progress_ratio
    if ratio is None:
        return None
    return round(ratio * 100, 1)


def is_overdue(goal: Goal, today) -> bool:
    if goal.is_completed or goal.deadline is None:
        return False
    return goal.deadline < today


def remaining_to_target(current: float | None, target: float | None) -> float | None:
    if target is None:
        return None
    cur = current or 0.0
    return round(max(0.0, float(target) - float(cur)), 2)
