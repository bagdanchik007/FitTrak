"""Personal-record application helpers."""

from app.domain.progress.services import format_pr_label, is_new_personal_record


def evaluate_candidate(
    *,
    exercise_name: str,
    previous_best_kg: float | None,
    weight_kg: float,
    reps: int,
) -> dict:
    is_pr = is_new_personal_record(previous_best_kg, weight_kg)
    return {
        "is_personal_record": is_pr,
        "label": format_pr_label(exercise_name, weight_kg, reps) if is_pr else None,
        "previous_best_kg": previous_best_kg,
        "candidate_kg": weight_kg,
    }
