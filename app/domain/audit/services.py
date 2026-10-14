"""Lightweight audit event shaping (no persistence required for demo)."""

from datetime import UTC, datetime


def build_audit_event(
    *,
    action: str,
    resource: str,
    resource_id: str | None = None,
    actor_id: str | None = None,
) -> dict:
    return {
        "action": action,
        "resource": resource,
        "resource_id": resource_id,
        "actor_id": actor_id,
        "at": datetime.now(UTC).isoformat(),
    }
