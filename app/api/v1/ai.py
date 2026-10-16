"""AI coaching endpoints (rule-based by default)."""

from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.application.services.ai_coach_service import answer_coach, build_workout_suggestion
from app.core.dependencies import CurrentUserId

router = APIRouter(prefix="/ai", tags=["AI Coach"])


class SuggestBody(BaseModel):
    recent_focuses: list[str] = Field(default_factory=list)
    experience: str = "intermediate"
    focus: str | None = None


class CoachBody(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000)


@router.post("/suggest-workout")
async def suggest_workout(body: SuggestBody, user_id: CurrentUserId) -> dict:
    """Suggest a session from rotation heuristics (auth required)."""
    _ = user_id
    return build_workout_suggestion(
        recent_focuses=body.recent_focuses,
        experience=body.experience,
        focus=body.focus,
    )


@router.post("/coach")
async def coach(body: CoachBody, user_id: CurrentUserId) -> dict:
    """Short coaching reply — OpenAI if configured, else rules."""
    _ = user_id
    return answer_coach(body.message)
