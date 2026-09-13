from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = Field(None, max_length=150)


class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=128)

    @field_validator("password")
    @classmethod
    def validate_password_strength(cls, v: str) -> str:
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one digit")
        if not any(c.isalpha() for c in v):
            raise ValueError("Password must contain at least one letter")
        return v


class UserUpdate(BaseModel):
    full_name: str | None = Field(None, max_length=150)
    password: str | None = Field(None, min_length=8, max_length=128)


class UserRead(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    is_active: bool
    created_at: datetime
    last_login_at: datetime | None = None


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    access_expires_in: int | None = None  # seconds
    refresh_expires_in: int | None = None  # seconds


class TokenPayload(BaseModel):
    sub: str | None = None
    type: str | None = None


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class PasswordChange(BaseModel):
    current_password: str = Field(..., min_length=8)
    new_password: str = Field(..., min_length=8, max_length=128)

# Password must include at least one letter and one digit
