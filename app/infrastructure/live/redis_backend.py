"""Optional Redis backend for live session snapshots."""

from __future__ import annotations

import json
from typing import Any


class RedisLiveBackend:
    """Thin wrapper; imports redis only when used."""

    def __init__(self, url: str) -> None:
        import redis

        self._client = redis.from_url(url, decode_responses=True)
        self._prefix = "fittrack:live:"

    def save_session(self, user_id: str, snapshot: dict[str, Any], ttl_seconds: int = 86400) -> None:
        key = f"{self._prefix}{user_id}"
        self._client.setex(key, ttl_seconds, json.dumps(snapshot))

    def load_session(self, user_id: str) -> dict[str, Any] | None:
        raw = self._client.get(f"{self._prefix}{user_id}")
        if not raw:
            return None
        return json.loads(raw)

    def delete_session(self, user_id: str) -> None:
        self._client.delete(f"{self._prefix}{user_id}")


def get_redis_backend():
    from app.core.config import get_settings

    settings = get_settings()
    if not settings.redis_url:
        return None
    try:
        return RedisLiveBackend(settings.redis_url)
    except Exception:
        return None
