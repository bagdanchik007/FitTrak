from app.domain.journal.services import mood_polarity

def test_mood_polarity():
    assert mood_polarity("great") == "positive"
    assert mood_polarity("bad") == "negative"
    assert mood_polarity("ok") == "neutral"
