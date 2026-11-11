from app.domain.export.mime import content_disposition

def test_cd():
    assert "workouts.csv" in content_disposition()
