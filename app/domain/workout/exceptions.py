"""Workout domain exceptions."""

from app.core.exceptions import NotFoundError


class WorkoutNotFoundError(NotFoundError):
    def __init__(self) -> None:
        super().__init__("Workout")
