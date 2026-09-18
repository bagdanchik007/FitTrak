"""Authz helpers (simple policies)."""

from uuid import UUID


def is_owner(resource_owner_id: UUID | None, actor_id: UUID) -> bool:
    if resource_owner_id is None:
        return False
    return resource_owner_id == actor_id


def can_modify_exercise(created_by: UUID | None, actor_id: UUID, is_superuser: bool = False) -> bool:
    if is_superuser:
        return True
    if created_by is None:
        return False  # system exercises: only superuser
    return created_by == actor_id
