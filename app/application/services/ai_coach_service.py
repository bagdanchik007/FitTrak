"""AI coach application service — rules always; optional OpenAI if configured."""

from __future__ import annotations

import json
import logging
import urllib.error
import urllib.request

from app.core.config import get_settings
from app.domain.ai.services import coach_reply, suggest_focus, suggest_session

logger = logging.getLogger("fittrack.ai")


def build_workout_suggestion(
    *,
    recent_focuses: list[str] | None = None,
    experience: str = "intermediate",
    focus: str | None = None,
) -> dict:
    chosen = focus or suggest_focus(recent_focuses=recent_focuses)
    session = suggest_session(focus=chosen, experience=experience)
    return session


def answer_coach(message: str) -> dict:
    settings = get_settings()
    api_key = getattr(settings, "openai_api_key", None)
    if api_key:
        try:
            text = _openai_chat(api_key, message)
            return {"reply": text, "engine": "openai"}
        except Exception:
            logger.exception("openai_coach_failed")
    return {"reply": coach_reply(message), "engine": "rules"}


def _openai_chat(api_key: str, message: str) -> str:
    body = json.dumps(
        {
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are FitTrack coach. Short, practical fitness advice. "
                        "No medical diagnosis. Reply in the user's language when clear."
                    ),
                },
                {"role": "user", "content": message[:2000]},
            ],
            "max_tokens": 300,
        }
    ).encode()
    req = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=body,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode())
    return data["choices"][0]["message"]["content"].strip()
