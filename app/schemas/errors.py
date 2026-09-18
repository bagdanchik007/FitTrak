"""Error response schemas for OpenAPI."""

from pydantic import BaseModel


class HTTPError(BaseModel):
    detail: str


class HTTPErrorWithRequestId(BaseModel):
    detail: str
    request_id: str | None = None
