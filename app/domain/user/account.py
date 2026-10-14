"""Account lifecycle pure helpers."""


def can_soft_delete(*, is_active: bool, is_superuser: bool) -> bool:
    """Superusers are protected from self soft-delete in the demo API."""
    if is_superuser:
        return False
    return is_active


def anonymized_email(user_id: str) -> str:
    short = user_id.replace("-", "")[:12]
    return f"deleted-{short}@fittrack.invalid"
