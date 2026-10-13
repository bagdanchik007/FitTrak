from app.domain.workout.services import truncate_notes

def test_truncate_notes():
    assert truncate_notes("  hi  ") == "hi"
    assert truncate_notes("x" * 10, max_len=5).endswith("…")
