"""Calculate volume for a single set."""

def set_volume_kg(*, reps: int | None, weight_kg: float | None) -> float:
    if not reps or weight_kg is None:
        return 0.0
    return float(reps) * float(weight_kg)
