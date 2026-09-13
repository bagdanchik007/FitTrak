import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_login_wrong_password_returns_401(client: AsyncClient):
    await client.post(
        "/api/v1/auth/register",
        json={"email": "wrongpw@test.com", "password": "SecurePass123!", "full_name": "W"},
    )
    resp = await client.post(
        "/api/v1/auth/login",
        data={"username": "wrongpw@test.com", "password": "TotallyWrong999!"},
    )
    assert resp.status_code == 401


@pytest.mark.asyncio
async def test_change_password_wrong_current_returns_400(client: AsyncClient):
    await client.post(
        "/api/v1/auth/register",
        json={"email": "chgpw@test.com", "password": "SecurePass123!", "full_name": "C"},
    )
    login = await client.post(
        "/api/v1/auth/login",
        data={"username": "chgpw@test.com", "password": "SecurePass123!"},
    )
    token = login.json()["access_token"]
    resp = await client.post(
        "/api/v1/auth/change-password",
        json={"current_password": "WrongCurrent1!", "new_password": "NewSecure99!"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert resp.status_code == 400

# change-password wrong current covered in same module
