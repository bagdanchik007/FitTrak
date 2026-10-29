from app.domain.notification.priority import priority_rank

def test_rank():
    assert priority_rank("high") < priority_rank("low")
