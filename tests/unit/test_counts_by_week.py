from datetime import date
from app.domain.workout.count_by_week import counts_by_week

def test_counts():
    d = date(2026, 1, 5)
    assert counts_by_week([d, d])[list(counts_by_week([d, d]).keys())[0]] == 2
