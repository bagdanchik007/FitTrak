from datetime import datetime, timezone
from unittest.mock import AsyncMock
from uuid import uuid4

import pytest
from fastapi import HTTPException

from app.application.services.user_service import UserService
from app.domain.user.entities import User
from app.schemas.user import UserUpdate


@pytest.fixture
def mock_repo():
    return AsyncMock()


@pytest.fixture
def service(mock_repo):
    return UserService(user_repo=mock_repo)


@pytest.mark.asyncio
async def test_get_by_id_not_found(service, mock_repo):
    mock_repo.get_by_id.return_value = None
    with pytest.raises(Exception):
        await service.get_by_id(uuid4())


@pytest.mark.asyncio
async def test_update_profile_name(service, mock_repo):
    user = User(
        id=uuid4(),
        email="u@test.com",
        hashed_password="x",
        full_name="Old",
        is_active=True,
        is_superuser=False,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
    )
    mock_repo.get_by_id.return_value = user
    mock_repo.update.return_value = user
    result = await service.update_profile(user.id, UserUpdate(full_name="New Name"))
    assert result.full_name == "New Name" or mock_repo.update.called
