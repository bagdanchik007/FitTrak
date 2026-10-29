from app.domain.workout.notes import truncate_notes

def test_short():
    assert truncate_notes("hi") == "hi"

def test_long():
    assert truncate_notes("x" * 200, max_len=20).endswith("…")
