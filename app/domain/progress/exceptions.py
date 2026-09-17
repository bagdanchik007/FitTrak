"""Progress domain exceptions."""

from app.core.exceptions import AppException


class ProgressCalculationError(AppException):
    def __init__(self, message: str = "Could not calculate progress") -> None:
        super().__init__(message)
