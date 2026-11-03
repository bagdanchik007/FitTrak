from app.domain.progress.pace import required_weekly_pace

def test_pace():
    assert required_weekly_pace(remaining=10, weeks_left=2) == 5.0
