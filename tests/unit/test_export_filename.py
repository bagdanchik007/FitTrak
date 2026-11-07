from datetime import date
from app.domain.export.filename import export_filename

def test_name():
    assert export_filename("Workouts!", day=date(2026, 1, 2)) == "Workouts-2026-01-02.csv"
