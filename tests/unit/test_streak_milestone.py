from app.domain.streak.milestone import milestone_reached, next_milestone

def test_next():
    assert next_milestone(5) == 7

def test_reached():
    assert milestone_reached(7) == 7
