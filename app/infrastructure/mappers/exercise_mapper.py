"""Map between ExerciseModel and Exercise entity."""

from app.domain.exercise.entities import Exercise
from app.infrastructure.database.models.exercise import ExerciseModel


def model_to_exercise(model: ExerciseModel) -> Exercise:
    return Exercise(
        id=model.id,
        name=model.name,
        description=model.description,
        muscle_group=model.muscle_group,
        equipment=model.equipment,
        created_by=model.created_by,
        created_at=model.created_at,
        updated_at=model.updated_at,
        deleted_at=model.deleted_at,
    )
