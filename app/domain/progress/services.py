"""Progress domain calculations."""

from app.domain.progress.entities import PersonalRecord


def sort_prs_by_weight(prs: list[PersonalRecord]) -> list[PersonalRecord]:
    return sorted(
        prs,
        key=lambda p: p.max_weight_kg or 0,
        reverse=True,
    )


def top_n_prs(prs: list[PersonalRecord], n: int = 5) -> list[PersonalRecord]:
    return sort_prs_by_weight(prs)[:n]


def is_new_personal_record(previous_best: float | None, candidate: float) -> bool:
    """Return True when candidate strictly exceeds a known previous best."""
    if previous_best is None:
        return True
    return candidate > previous_best


def format_pr_label(exercise_name: str, weight_kg: float, reps: int) -> str:
    return f"{exercise_name}: {weight_kg:g} kg x {reps}"
