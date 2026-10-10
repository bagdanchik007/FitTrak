from app.domain.streak.services import streak_milestone

def test_streak_milestone():
    assert streak_milestone(3) is None
    assert streak_milestone(7) == "7_days"
    assert streak_milestone(45) == "30_days"
