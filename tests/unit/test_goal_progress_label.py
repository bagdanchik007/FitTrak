from app.domain.goal.progress_label import progress_label

def test_completed():
    assert progress_label(10, 10) == "completed"
