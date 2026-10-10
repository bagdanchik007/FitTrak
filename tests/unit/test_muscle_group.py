from app.domain.exercise.services import normalize_muscle_group

def test_normalize_muscle_group():
    assert normalize_muscle_group("Pectorals") == "chest"
    assert normalize_muscle_group("lats") == "back"
    assert normalize_muscle_group(None) is None
