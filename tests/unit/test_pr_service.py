from app.application.services.pr_service import evaluate_candidate


def test_new_pr_when_no_previous():
    result = evaluate_candidate(exercise_name="Squat", previous_best_kg=None, weight_kg=100, reps=5)
    assert result["is_personal_record"] is True
    assert "Squat" in result["label"]


def test_not_pr_when_lower():
    result = evaluate_candidate(exercise_name="Bench", previous_best_kg=80, weight_kg=75, reps=5)
    assert result["is_personal_record"] is False
    assert result["label"] is None
