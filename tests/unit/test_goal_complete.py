from app.domain.goal.completion import is_goal_complete

def test_done():
    assert is_goal_complete(current=10, target=10)
