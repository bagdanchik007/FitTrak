"""Human labels for activity feed event types."""

LABELS = {
    "workout": "Logged a workout",
    "workout_created": "Logged a workout",
    "body_weight": "Logged body weight",
    "goal_completed": "Completed a goal",
    "pr_set": "Hit a personal record",
    "streak_milestone": "Streak milestone",
}


def activity_label(event_type: str | None) -> str:
    key = (event_type or "").strip().lower()
    return LABELS.get(key, "Activity")
