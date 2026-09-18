"""Map WorkoutModel to domain Workout."""

from app.domain.workout.entities import Workout, WorkoutSet
from app.infrastructure.database.models.workout import WorkoutModel


def model_to_workout(model: WorkoutModel) -> Workout:
    sets = [
        WorkoutSet(
            id=s.id,
            workout_id=s.workout_id,
            exercise_id=s.exercise_id,
            set_number=s.set_number,
            reps=s.reps,
            weight_kg=s.weight_kg,
            rpe=s.rpe,
            notes=s.notes,
        )
        for s in (model.sets or [])
    ]
    return Workout(
        id=model.id,
        user_id=model.user_id,
        title=model.title,
        notes=model.notes,
        performed_at=model.performed_at,
        duration_minutes=model.duration_minutes,
        created_at=model.created_at,
        updated_at=model.updated_at,
        deleted_at=model.deleted_at,
        sets=sets,
    )
