"""Favorite application helpers."""

from uuid import UUID


def favorite_key(user_id: UUID, exercise_id: UUID) -> str:
    return f"{user_id}:{exercise_id}"
