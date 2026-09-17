"""Exercise domain exceptions."""

from app.core.exceptions import ConflictError, ForbiddenError, NotFoundError


class ExerciseNotFoundError(NotFoundError):
    def __init__(self) -> None:
        super().__init__("Exercise")


class ExerciseInUseError(ConflictError):
    def __init__(self) -> None:
        super().__init__("Exercise is referenced in workout sets and cannot be deleted")


class ExercisePermissionError(ForbiddenError):
    def __init__(self) -> None:
        super().__init__("Not enough permissions to modify this exercise")
