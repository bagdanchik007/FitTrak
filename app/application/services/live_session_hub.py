"""In-memory hub for live workout session WebSocket connections."""

from __future__ import annotations

import asyncio
import json
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any
from fastapi import WebSocket

from app.domain.live.services import normalize_live_event
from app.infrastructure.live.redis_backend import get_redis_backend


@dataclass
class LiveSessionState:
    user_id: str
    started_at: str
    exercise_name: str | None = None
    set_count: int = 0
    last_event: str = "started"
    metadata: dict[str, Any] = field(default_factory=dict)


class LiveSessionHub:
    """Process-local hub (sufficient for single-instance / demo deployments)."""

    def __init__(self) -> None:
        self._connections: dict[str, set[WebSocket]] = defaultdict(set)
        self._sessions: dict[str, LiveSessionState] = {}
        self._lock = asyncio.Lock()

    async def connect(self, user_id: str, websocket: WebSocket) -> None:
        await websocket.accept()
        async with self._lock:
            self._connections[user_id].add(websocket)
            if user_id not in self._sessions:
                self._sessions[user_id] = LiveSessionState(
                    user_id=user_id,
                    started_at=datetime.now(UTC).isoformat(),
                )

    async def disconnect(self, user_id: str, websocket: WebSocket) -> None:
        async with self._lock:
            conns = self._connections.get(user_id)
            if not conns:
                return
            conns.discard(websocket)
            if not conns:
                self._connections.pop(user_id, None)
                self._sessions.pop(user_id, None)

    async def handle_event(self, user_id: str, payload: dict[str, Any]) -> dict[str, Any]:
        event = normalize_live_event(str(payload.get("event") or "ping"))
        async with self._lock:
            state = self._sessions.get(user_id)
            if state is None:
                state = LiveSessionState(
                    user_id=user_id,
                    started_at=datetime.now(UTC).isoformat(),
                )
                self._sessions[user_id] = state
            if event == "set_logged":
                state.set_count += 1
                state.last_event = "set_logged"
                if payload.get("exercise_name"):
                    state.exercise_name = str(payload["exercise_name"])
            elif event == "exercise_changed":
                state.exercise_name = str(payload.get("exercise_name") or state.exercise_name)
                state.last_event = "exercise_changed"
            elif event == "ended":
                state.last_event = "ended"
            else:
                state.last_event = event
            snapshot = {
                "user_id": state.user_id,
                "started_at": state.started_at,
                "exercise_name": state.exercise_name,
                "set_count": state.set_count,
                "last_event": state.last_event,
                "server_time": datetime.now(UTC).isoformat(),
            }
        backend = get_redis_backend()
        if backend is not None:
            try:
                backend.save_session(user_id, snapshot)
            except Exception:
                pass
        await self.broadcast(user_id, {"type": "session_update", "session": snapshot})
        return snapshot

    async def broadcast(self, user_id: str, message: dict[str, Any]) -> None:
        data = json.dumps(message)
        async with self._lock:
            targets = list(self._connections.get(user_id, set()))
        stale: list[WebSocket] = []
        for ws in targets:
            try:
                await ws.send_text(data)
            except Exception:
                stale.append(ws)
        for ws in stale:
            await self.disconnect(user_id, ws)

    def active_session(self, user_id: str) -> dict[str, Any] | None:
        state = self._sessions.get(user_id)
        if state is None:
            return None
        return {
            "user_id": state.user_id,
            "started_at": state.started_at,
            "exercise_name": state.exercise_name,
            "set_count": state.set_count,
            "last_event": state.last_event,
        }


live_session_hub = LiveSessionHub()
