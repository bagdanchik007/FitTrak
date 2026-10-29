from app.domain.recovery.suggestion import suggest_rest

def recovery_hint(trained_last_7_days: int) -> dict:
    return suggest_rest(trained_last_7_days=trained_last_7_days)
