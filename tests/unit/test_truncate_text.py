from app.domain.text.truncate import truncate

def test_trunc():
    assert truncate("abcdef", max_len=4).endswith("…")
