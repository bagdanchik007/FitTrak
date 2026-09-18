"""Standard API response helpers."""

from typing import Any, Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class SuccessResponse(BaseModel, Generic[T]):
    data: T
    message: str | None = None


class ErrorBody(BaseModel):
    detail: str
    request_id: str | None = None
    code: str | None = None


def error_dict(detail: str, request_id: str | None = None, code: str | None = None) -> dict[str, Any]:
    body: dict[str, Any] = {"detail": detail}
    if request_id:
        body["request_id"] = request_id
    if code:
        body["code"] = code
    return body
