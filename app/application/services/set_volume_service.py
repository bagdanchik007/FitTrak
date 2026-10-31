from app.domain.workout.set_volume import set_volume_kg

def volume_for_set(reps: int | None, weight_kg: float | None) -> dict:
    return {"volume_kg": set_volume_kg(reps=reps, weight_kg=weight_kg)}
