"""Simple in-memory rate limiting helper (portfolio-friendly, not production-grade)."""

import time
from collections import defaultdict
from threading import Lock

from fastapi import HTTPException, Request, status

# path -> list of timestamps
_hits: dict[str, list[float]] = defaultdict(list)
_lock = Lock()


def rate_limit(max_requests: int = 60, window_seconds: int = 60):
    """Dependency factory for basic IP-based rate limiting."""

    async def dependency(request: Request) -> None:
        client = request.client.host if request.client else "unknown"
        key = f"{client}:{request.url.path}"
        now = time.time()
        with _lock:
            window = [t for t in _hits[key] if now - t < window_seconds]
            if len(window) >= max_requests:
                raise HTTPException(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    detail="Rate limit exceeded. Try again later.",
                )
            window.append(now)
            _hits[key] = window

    return dependency
