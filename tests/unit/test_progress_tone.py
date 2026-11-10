from app.domain.color.tone import progress_tone

def test_tone():
    assert progress_tone(100) == "success"
