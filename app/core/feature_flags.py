"""Central feature flag map (mirrors /meta/features)."""

FEATURES = {
    "refresh_tokens": True,
    "progress_tracking": True,
    "stats_dashboard": True,
    "rate_limiting": True,
    "soft_deletes": True,
    "goals": True,
    "body_weight": True,
    "templates": True,
    "preferences": True,
    "activity_feed": True,
    "csv_export": True,
    "journal": True,
    "favorites": True,
    "streaks": True,
    "weekly_summary": True,
}


def is_enabled(name: str) -> bool:
    return bool(FEATURES.get(name, False))
