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
    "goal_progress": True,
    "pr_check": True,
    "journal_search": True,
    "template_duplicate": True,
    "workout_metrics": True,
    "goal_reopen": True,
    "preferences_reset": True,
    "recovery_status": True,
    "exercise_search": True,
    "journal_mood_stats": True,
    "weekly_goal_progress": True,
    "favorite_exists": True,
    "goals_with_progress": True,
    "density_bands": True,
    "consistency_score": True,
    "volume_load_bands": True,
    "body_weight_trend": True,
    "average_rpe": True,
    "goal_status_labels": True,
    "training_days": True,
    "frequency_band": True,
    "pr_improvement_pct": True,
    "favorites_capacity": True,
    "duration_band": True,
    "mood_polarity": True,
    "pagination_meta": True,
    "preference_normalization": True,
}


def is_enabled(name: str) -> bool:
    return bool(FEATURES.get(name, False))


# Keep in sync with /meta/features response
