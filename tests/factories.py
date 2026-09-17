"""Test data factories (simple, no external deps)."""

from datetime import date, datetime, timezone
from uuid import uuid4

from app.domain.user.entities import User
from app.domain.exercise.entities import Exercise
from app.schemas.user import UserCreate
from app.schemas.exercise import ExerciseCreate
from app.schemas.workout import WorkoutCreate, WorkoutSetCreate


def make_user_create(
    email: str = "factory@example.com",
    password: str = "SecurePass123!",
    full_name: str = "Factory User",
) -> UserCreate:
    return UserCreate(email=email, password=password, full_name=full_name)


def make_user_entity(email: str = "entity@example.com") -> User:
    now = datetime.now(timezone.utc)
    return User(
        id=uuid4(),
        email=email,
        hashed_password="hashed",
        full_name="Entity User",
        is_active=True,
        is_superuser=False,
        created_at=now,
        updated_at=now,
    )


def make_exercise_create(name: str = "Factory Lift") -> ExerciseCreate:
    return ExerciseCreate(name=name, muscle_group="chest", equipment="barbell")


def make_exercise_entity(name: str = "Entity Lift") -> Exercise:
    now = datetime.now(timezone.utc)
    return Exercise(
        id=uuid4(),
        name=name,
        description=None,
        muscle_group="back",
        equipment="barbell",
        created_by=None,
        created_at=now,
        updated_at=now,
    )


def make_workout_create(exercise_id) -> WorkoutCreate:
    return WorkoutCreate(
        title="Factory Session",
        performed_at=date.today(),
        duration_minutes=45,
        sets=[
            WorkoutSetCreate(
                exercise_id=exercise_id,
                set_number=1,
                reps=8,
                weight_kg=60.0,
            )
        ],
    )
