"""Favorite pure helpers."""


def favorites_capacity_hint(count: int, soft_limit: int = 50) -> str:
    if count >= soft_limit:
        return "at_capacity"
    if count >= soft_limit * 0.8:
        return "near_capacity"
    return "ok"
