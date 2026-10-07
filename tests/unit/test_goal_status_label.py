from app.domain.goal.progress import goal_status_label

def test_goal_status_label():
    assert goal_status_label(is_completed=True, is_overdue=False, percent=100) == "completed"
    assert goal_status_label(is_completed=False, is_overdue=True, percent=50) == "overdue"
    assert goal_status_label(is_completed=False, is_overdue=False, percent=80) == "near_target"
