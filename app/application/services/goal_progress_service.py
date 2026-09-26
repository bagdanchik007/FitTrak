"""Goal progress application facade."""

from datetime import date

from app.domain.goal.entities import Goal
from app.domain.goal.progress import is_overdue, percent_complete


def goal_status(goal: Goal, today: date | None = None) -> dict:
    today = today or date.today()
    return {
        "percent_complete": percent_complete(goal),
        "is_overdue": is_overdue(goal, today),
        "is_completed": goal.is_completed,
    }
