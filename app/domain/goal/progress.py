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
