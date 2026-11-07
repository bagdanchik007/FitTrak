from datetime import date
from app.domain.scheduling.reminder import should_remind

def test_remind():
    assert should_remind(last_trained=date(2026, 1, 1), today=date(2026, 1, 5), gap_days=2)
