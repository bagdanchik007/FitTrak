from app.domain.workout.export_row import workout_export_row

def test_row():
    row = workout_export_row(
        id="1",
        title="Push",
        performed_at="2026-01-01",
        duration_minutes=60,
        total_volume_kg=1000,
        notes="ok",
    )
    assert row[1] == "Push"
