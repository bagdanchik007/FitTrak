from app.domain.journal.mood_score import mood_score

def test_good():
    assert mood_score("good") == 4
