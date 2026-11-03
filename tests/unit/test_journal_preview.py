from app.domain.journal.preview import journal_preview

def test_trunc():
    assert journal_preview("x" * 200, max_len=20).endswith("…")
