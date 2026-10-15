"""System / readiness pure helpers."""

from app.core.version import __version__


def build_health_payload(*, database_ok: bool | None = None) -> dict:
    payload: dict = {
        "status": "ok" if database_ok is not False else "degraded",
        "version": __version__,
        "service": "fittrack",
    }
    if database_ok is not None:
        payload["database"] = "up" if database_ok else "down"
    return payload
