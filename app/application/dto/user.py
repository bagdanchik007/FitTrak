"""User-related internal DTOs."""

from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class UpdateProfileDTO(BaseModel):
    user_id: UUID
    full_name: str | None = Field(None, max_length=150)
    password: str | None = Field(None, min_length=8, max_length=128)


class PublicUserDTO(BaseModel):
    id: UUID
    full_name: str | None
    email: EmailStr | None = None  # omit in strict public APIs if desired
