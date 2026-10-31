from app.domain.session.rest_timer import suggested_rest_seconds

def rest_suggestion(rpe: float | None = None, is_compound: bool = True) -> dict:
    return {
        "rest_seconds": suggested_rest_seconds(rpe=rpe, is_compound=is_compound),
        "rpe": rpe,
        "is_compound": is_compound,
    }
