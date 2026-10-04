"""Weekly workout-goal progress against user preferences."""

from datetime import date

from app.domain.summary.services import progress_toward_weekly_goal, weekly_goal_label


def weekly_goal_status(
    workouts_done: int,
    weekly_goal: int,
    *,
    from_date: date | None = None,
    to_date: date | None = None,
) -> dict:
    ratio = progress_toward_weekly_goal(workouts_done, weekly_goal)
    return {
        "workouts_done": workouts_done,
        "weekly_goal": weekly_goal,
        "progress_ratio": ratio,
        "remaining": max(0, weekly_goal - workouts_done),
        "goal_met": workouts_done >= weekly_goal if weekly_goal > 0 else False,
        "status": weekly_goal_label(workouts_done, weekly_goal),
        "from_date": from_date.isoformat() if from_date else None,
        "to_date": to_date.isoformat() if to_date else None,
    }
