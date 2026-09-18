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
