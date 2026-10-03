"""Weekly workout-goal progress against user preferences."""

from app.domain.summary.services import progress_toward_weekly_goal


def weekly_goal_status(workouts_done: int, weekly_goal: int) -> dict:
    ratio = progress_toward_weekly_goal(workouts_done, weekly_goal)
    return {
        "workouts_done": workouts_done,
        "weekly_goal": weekly_goal,
        "progress_ratio": ratio,
        "remaining": max(0, weekly_goal - workouts_done),
        "goal_met": workouts_done >= weekly_goal if weekly_goal > 0 else False,
    }
