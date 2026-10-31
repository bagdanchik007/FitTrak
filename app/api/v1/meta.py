"""Meta endpoints (version, feature flags placeholder)."""

from fastapi import APIRouter

from app.core.config import get_settings
from app.core.feature_flags import FEATURES
from app.core.version import __version__
from app.core.build_info import API_COMPAT, BUILD_CHANNEL
from app.schemas.meta import VersionResponse

router = APIRouter(prefix="/meta", tags=["Meta"])
settings = get_settings()


@router.get("/version", response_model=VersionResponse)
async def version() -> VersionResponse:
    return VersionResponse(
        app=settings.app_name,
        version=__version__,
        environment=settings.app_env,
    )


@router.get("/features")
async def features() -> dict[str, bool]:
    return dict(FEATURES)


@router.get("/build")
async def build_info() -> dict[str, str]:
    return {"version": __version__, "api": API_COMPAT, "channel": BUILD_CHANNEL}


@router.get("/pagination")
async def pagination_defaults() -> dict:
    from app.core.limits import DEFAULT_PAGE_SIZE, MAX_PAGE_SIZE

    return {"default_page_size": DEFAULT_PAGE_SIZE, "max_page_size": MAX_PAGE_SIZE}


@router.post("/password-strength")
async def check_password_strength(payload: dict) -> dict:
    """Client-side helper: score a candidate password without storing it."""
    from app.domain.user.password_policy import (
        is_password_acceptable,
        password_strength_label,
        password_strength_score,
    )

    password = str(payload.get("password") or "")
    score = password_strength_score(password)
    return {
        "score": score,
        "label": password_strength_label(score),
        "acceptable": is_password_acceptable(password),
    }

@router.get("/timezones")
async def list_common_timezones() -> dict:
    return {
        "timezones": [
            "UTC",
            "Europe/Berlin",
            "Europe/Kyiv",
            "America/New_York",
            "America/Los_Angeles",
            "Asia/Tokyo",
        ]
    }

@router.get("/audit-example")
async def audit_example() -> dict:
    from app.domain.audit.services import build_audit_event

    return build_audit_event(action="read", resource="meta", resource_id="audit-example")

@router.get("/duration-band")
async def meta_duration_band(minutes: int | None = None) -> dict:
    from app.application.services.duration_band_service import band_for_minutes
    return band_for_minutes(minutes)


@router.get("/goal-progress-label")
async def meta_goal_progress_label(current: float = 0, target: float = 1) -> dict:
    from app.domain.goal.progress_label import progress_label
    return {"label": progress_label(current, target), "current": current, "target": target}

@router.get("/recovery-hint")
async def meta_recovery_hint(trained_last_7_days: int = 0) -> dict:
    from app.application.services.recovery_hint_service import recovery_hint
    return recovery_hint(trained_last_7_days)


@router.get("/page-meta")
async def meta_page_meta(total: int = 0, skip: int = 0, limit: int = 20) -> dict:
    from app.application.services.pagination_service import build_page_meta
    return build_page_meta(total, skip, limit)

@router.get("/notes-preview")
async def meta_notes_preview(notes: str = "") -> dict:
    from app.application.services.notes_preview_service import notes_preview
    return notes_preview(notes)


@router.get("/activity-label")
async def meta_activity_label(event_type: str = "") -> dict:
    from app.domain.activity.feed_label import activity_label
    return {"event_type": event_type, "label": activity_label(event_type)}

@router.get("/set-volume")
async def meta_set_volume(reps: int | None = None, weight_kg: float | None = None) -> dict:
    from app.application.services.set_volume_service import volume_for_set
    return volume_for_set(reps, weight_kg)


@router.get("/rest-suggestion")
async def meta_rest_suggestion(rpe: float | None = None, is_compound: bool = True) -> dict:
    from app.application.services.rest_timer_service import rest_suggestion
    return rest_suggestion(rpe=rpe, is_compound=is_compound)


@router.get("/volume-delta")
async def meta_volume_delta(current: float = 0, previous: float = 0) -> dict:
    from app.domain.progress.weekly_delta import volume_delta_pct
    pct = volume_delta_pct(current, previous)
    return {"current": current, "previous": previous, "delta_pct": pct}
