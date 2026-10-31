from datetime import date
from app.domain.goal.deadline_status import deadline_status

def test_overdue():
    assert deadline_status(date(2020, 1, 1), today=date(2020, 1, 2)) == "overdue"

def test_soon():
    assert deadline_status(date(2020, 1, 5), today=date(2020, 1, 1)) == "due_soon"
