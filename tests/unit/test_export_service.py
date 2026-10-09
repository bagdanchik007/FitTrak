from app.application.services.export_service import format_csv_row, workout_csv_header

def test_workout_csv_header():
    assert "performed_at" in workout_csv_header()

def test_format_csv_row():
    assert format_csv_row(["a", None, "b,c"]) == 'a,,"b,c"'
