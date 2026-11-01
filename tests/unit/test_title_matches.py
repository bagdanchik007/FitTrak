from app.domain.workout.search import title_matches

def test_match():
    assert title_matches("Push Day", "push")
    assert not title_matches("Leg Day", "push")
