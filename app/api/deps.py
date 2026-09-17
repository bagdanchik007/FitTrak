"""Centralized FastAPI dependency factories."""

from app.application.services.auth_service import AuthService
from app.application.services.exercise_service import ExerciseService
from app.application.services.progress_service import ProgressService
from app.application.services.user_service import UserService
from app.application.services.workout_service import WorkoutService
from app.core.dependencies import DbSession
from app.infrastructure.repositories.exercise_repository import SQLAlchemyExerciseRepository
from app.infrastructure.repositories.progress_repository import SQLAlchemyProgressRepository
from app.infrastructure.repositories.user_repository import SQLAlchemyUserRepository
from app.infrastructure.repositories.workout_repository import SQLAlchemyWorkoutRepository


def get_auth_service(db: DbSession) -> AuthService:
    return AuthService(user_repo=SQLAlchemyUserRepository(db))


def get_user_service(db: DbSession) -> UserService:
    return UserService(user_repo=SQLAlchemyUserRepository(db))


def get_exercise_service(db: DbSession) -> ExerciseService:
    return ExerciseService(repo=SQLAlchemyExerciseRepository(db))


def get_workout_service(db: DbSession) -> WorkoutService:
    return WorkoutService(repo=SQLAlchemyWorkoutRepository(db))


def get_progress_service(db: DbSession) -> ProgressService:
    return ProgressService(repo=SQLAlchemyProgressRepository(db))
