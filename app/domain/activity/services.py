"""Activity feed pure helpers."""


def sort_activity_items(items: list[dict], limit: int = 20) -> list[dict]:
    ordered = sorted(items, key=lambda x: x.get("occurred_on") or "", reverse=True)
    return ordered[: max(1, limit)]


def activity_type_label(activity_type: str | None) -> str:
    mapping = {
        "workout": "Workout",
        "goal": "Goal",
        "journal": "Journal",
        "body_weight": "Body weight",
    }
    if not activity_type:
        return "Activity"
    return mapping.get(activity_type, activity_type.replace("_", " ").title())
