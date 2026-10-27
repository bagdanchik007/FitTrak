"""AI coaching endpoints (rule-based by default)."""

from fastapi import APIRouter
from pydantic import BaseModel, Field
from sqlalchemy import select

from app.application.services.ai_coach_service import answer_coach, build_workout_suggestion
from app.core.dependencies import CurrentUserId, DbSession
from app.infrastructure.database.models.workout import WorkoutModel

router = APIRouter(prefix="/ai", tags=["AI Coach"])


class SuggestBody(BaseModel):
    recent_focuses: list[str] = Field(default_factory=list)
    experience: str = "intermediate"
    focus: str | None = None
    use_history: bool = True


class CoachBody(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000)


@router.post("/suggest-workout")
async def suggest_workout(
    body: SuggestBody,
    user_id: CurrentUserId,
    db: DbSession,
) -> dict:
    """Suggest a session; optionally rotate away from recent workout titles."""
    titles: list[str] = []
    if body.use_history:
        stmt = (
            select(WorkoutModel.title)
            .where(
                WorkoutModel.user_id == user_id,
                WorkoutModel.deleted_at.is_(None),
            )
            .order_by(WorkoutModel.performed_at.desc())
            .limit(10)
        )
        rows = (await db.execute(stmt)).scalars().all()
        titles = [str(t) for t in rows if t]
    return build_workout_suggestion(
        recent_focuses=body.recent_focuses,
        recent_titles=titles or None,
        experience=body.experience,
        focus=body.focus,
    )


@router.post("/coach")
async def coach(body: CoachBody, user_id: CurrentUserId) -> dict:
    """Short coaching reply — OpenAI if configured, else rules."""
    _ = user_id
    return answer_coach(body.message)
