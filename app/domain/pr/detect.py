"""Detect personal records from a sequence of lift samples."""

def is_pr(*, weight_kg: float, previous_best: float | None) -> bool:
    if previous_best is None:
        return True
    return weight_kg > previous_best


def best_of(weights: list[float]) -> float | None:
    return max(weights) if weights else None
