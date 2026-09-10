import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_workout_with_sets(client: AsyncClient):
    await client.post(
        "/api/v1/auth/register",
        json={"email": "wo@test.com", "password": "SecurePass123!", "full_name": "WO User"},
    )
    login = await client.post(
        "/api/v1/auth/login",
        data={"username": "wo@test.com", "password": "SecurePass123!"},
    )
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Create exercise first
    ex = await client.post(
        "/api/v1/exercises",
        json={"name": "Squat", "muscle_group": "legs"},
        headers=headers,
    )
    exercise_id = ex.json()["id"]

    # Create workout
    resp = await client.post(
        "/api/v1/workouts",
        json={
            "title": "Leg Day",
            "performed_at": "2026-09-01",
            "duration_minutes": 50,
            "sets": [
                {"exercise_id": exercise_id, "set_number": 1, "reps": 8, "weight_kg": 100},
                {"exercise_id": exercise_id, "set_number": 2, "reps": 6, "weight_kg": 110},
            ],
        },
        headers=headers,
    )
    assert resp.status_code == 201
    data = resp.json()
    assert data["title"] == "Leg Day"
    assert len(data["sets"]) == 2
