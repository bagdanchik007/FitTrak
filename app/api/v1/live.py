"""WebSocket live workout session tracking."""

import json

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.application.services.live_session_hub import live_session_hub
from app.core.dependencies import CurrentUserId
from app.core.security import decode_token

router = APIRouter(tags=["Live Session"])


def _user_from_token(token: str) -> str | None:
    payload = decode_token(token)
    if payload is None:
        return None
    if payload.get("type") == "refresh":
        return None
    sub = payload.get("sub")
    return str(sub) if sub else None


@router.websocket("/ws/live-session")
async def live_session_ws(websocket: WebSocket) -> None:
    """Authenticate via query param `token` (JWT access token)."""
    token = websocket.query_params.get("token")
    if not token:
        await websocket.close(code=4401)
        return
    user_id = _user_from_token(token)
    if not user_id:
        await websocket.close(code=4401)
        return

    await live_session_hub.connect(user_id, websocket)
    await websocket.send_text(
        json.dumps({"type": "connected", "session": live_session_hub.active_session(user_id)})
    )
    try:
        while True:
            raw = await websocket.receive_text()
            try:
                payload = json.loads(raw)
            except json.JSONDecodeError:
                await websocket.send_text(json.dumps({"type": "error", "detail": "invalid_json"}))
                continue
            snapshot = await live_session_hub.handle_event(
                user_id, payload if isinstance(payload, dict) else {}
            )
            await websocket.send_text(json.dumps({"type": "ack", "session": snapshot}))
    except WebSocketDisconnect:
        await live_session_hub.disconnect(user_id, websocket)


@router.get("/live-session/status")
async def live_session_status(user_id: CurrentUserId) -> dict:
    """HTTP snapshot of the caller's active live session (if any)."""
    session = live_session_hub.active_session(str(user_id))
    return {"active": session is not None, "session": session}
