import asyncio
from app.application.services.live_session_hub import LiveSessionHub

def test_handle_event_set_logged():
    hub = LiveSessionHub()

    async def run():
        snap = await hub.handle_event("user-1", {"event": "set_logged", "exercise_name": "Bench"})
        assert snap["set_count"] == 1
        assert snap["exercise_name"] == "Bench"
        assert hub.active_session("user-1") is not None

    asyncio.run(run())
