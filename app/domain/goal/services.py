from app.domain.goal.entities import Goal


def is_goal_achieved(goal: Goal) -> bool:
    if goal.is_completed:
        return True
    if goal.target_value is None or goal.current_value is None:
        return False
    return goal.current_value >= goal.target_value


def remaining_to_target(goal: Goal) -> float | None:
    if goal.target_value is None or goal.current_value is None:
        return None
    return max(0.0, goal.target_value - goal.current_value)
