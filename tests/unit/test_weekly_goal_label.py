from app.domain.summary.services import weekly_goal_label


def test_weekly_goal_labels():
    assert weekly_goal_label(0, 3) == "not_started"
    assert weekly_goal_label(1, 3) == "in_progress"
    assert weekly_goal_label(3, 3) == "met"
    assert weekly_goal_label(1, 0) == "no_goal"
