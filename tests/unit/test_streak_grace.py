from app.domain.streak.grace import streak_survives_grace

def test_grace():
    assert streak_survives_grace(days_missed=1)
    assert not streak_survives_grace(days_missed=3)
