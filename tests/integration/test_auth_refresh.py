import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_refresh_token_flow(client: AsyncClient):
    await client.post(
        "/api/v1/auth/register",
        json={"email": "refresh@test.com", "password": "SecurePass123!", "full_name": "R"},
    )
    login = await client.post(
        "/api/v1/auth/login",
        data={"username": "refresh@test.com", "password": "SecurePass123!"},
    )
    assert login.status_code == 200
    tokens = login.json()
    assert "refresh_token" in tokens

    resp = await client.post(
        "/api/v1/auth/refresh",
        json={"refresh_token": tokens["refresh_token"]},
    )
    assert resp.status_code == 200
    new_tokens = resp.json()
    assert "access_token" in new_tokens
    assert "refresh_token" in new_tokens


@pytest.mark.asyncio
async def test_refresh_with_invalid_token(client: AsyncClient):
    resp = await client.post(
        "/api/v1/auth/refresh",
        json={"refresh_token": "not.a.valid.token"},
    )
    assert resp.status_code == 401
