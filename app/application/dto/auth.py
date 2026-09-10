"""Auth-related DTOs (kept for potential internal use)."""

from pydantic import BaseModel, EmailStr, Field


class RegisterDTO(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    full_name: str | None = None


class LoginDTO(BaseModel):
    email: EmailStr
    password: str
