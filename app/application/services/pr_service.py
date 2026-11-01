from app.domain.pr.detect import best_of, is_pr

def evaluate_pr(weight_kg: float, history: list[float]) -> dict:
    previous = best_of(history)
    return {
        "weight_kg": weight_kg,
        "previous_best": previous,
        "is_pr": is_pr(weight_kg=weight_kg, previous_best=previous),
    }
