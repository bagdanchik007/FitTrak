from app.domain.time_util.seconds import format_mmss

def test_fmt():
    assert format_mmss(65) == "1:05"
