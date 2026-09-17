"""User domain exceptions."""

from app.core.exceptions import ConflictError, NotFoundError, UnauthorizedError


class UserNotFoundError(NotFoundError):
    def __init__(self) -> None:
        super().__init__("User")


class EmailAlreadyExistsError(ConflictError):
    def __init__(self) -> None:
        super().__init__("A user with this email already exists")


class InvalidCredentialsError(UnauthorizedError):
    def __init__(self) -> None:
        super().__init__("Incorrect email or password")


class InactiveUserError(UnauthorizedError):
    def __init__(self) -> None:
        super().__init__("Inactive user")
