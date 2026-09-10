"""Custom application exceptions."""

from fastapi import HTTPException, status


class AppException(Exception):
    """Base application exception."""

    def __init__(self, message: str = "An application error occurred") -> None:
        self.message = message
        super().__init__(self.message)


class NotFoundError(AppException):
    """Resource was not found."""

    def __init__(self, resource: str = "Resource") -> None:
        super().__init__(f"{resource} not found")


class ConflictError(AppException):
    """Resource already exists or conflict occurred."""

    def __init__(self, message: str = "Resource already exists") -> None:
        super().__init__(message)


class UnauthorizedError(AppException):
    """Authentication failed."""

    def __init__(self, message: str = "Could not validate credentials") -> None:
        super().__init__(message)


class ForbiddenError(AppException):
    """User is not allowed to perform this action."""

    def __init__(self, message: str = "Not enough permissions") -> None:
        super().__init__(message)


def to_http_exception(exc: AppException) -> HTTPException:
    """Map domain exceptions to FastAPI HTTPExceptions."""
    mapping = {
        NotFoundError: status.HTTP_404_NOT_FOUND,
        ConflictError: status.HTTP_409_CONFLICT,
        UnauthorizedError: status.HTTP_401_UNAUTHORIZED,
        ForbiddenError: status.HTTP_403_FORBIDDEN,
    }
    status_code = mapping.get(type(exc), status.HTTP_400_BAD_REQUEST)
    return HTTPException(status_code=status_code, detail=exc.message)
