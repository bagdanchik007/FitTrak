"""Unit tests for AuthService (with mocked repository)."""

from datetime import datetime, timezone
from unittest.mock import AsyncMock
from uuid import uuid4

import pytest
from fastapi import HTTPException

from app.application.services.auth_service import AuthService
from app.domain.user.entities import User
from app.schemas.user import UserCreate


@pytest.fixture
def mock_repo():
    return AsyncMock()


@pytest.fixture
def service(mock_repo):
    return AuthService(user_repo=mock_repo)


@pytest.mark.asyncio
async def test_register_success(service, mock_repo):
    mock_repo.get_by_email.return_value = None
    created_user = User(
        id=uuid4(),
        email="new@example.com",
        hashed_password="hashed",
        full_name="New User",
        is_active=True,
        is_superuser=False,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
    )
    mock_repo.create.return_value = created_user

    result = await service.register(
        UserCreate(email="new@example.com", password="SecurePass123!", full_name="New User")
    )

    assert result.email == "new@example.com"
    mock_repo.create.assert_called_once()


@pytest.mark.asyncio
async def test_register_duplicate_email(service, mock_repo):
    mock_repo.get_by_email.return_value = User(
        id=uuid4(),
        email="exists@example.com",
        hashed_password="x",
        full_name=None,
        is_active=True,
        is_superuser=False,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
    )

    with pytest.raises(HTTPException) as exc:
        await service.register(
            UserCreate(email="exists@example.com", password="SecurePass123!")
        )
    assert exc.value.status_code == 409
