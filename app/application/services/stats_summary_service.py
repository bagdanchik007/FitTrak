from app.domain.stats_util.average import safe_average
from app.domain.stats_util.max_min import safe_max, safe_min

def volume_summary(volumes: list[float]) -> dict:
    return {
        "avg": safe_average(volumes),
        "max": safe_max(volumes),
        "min": safe_min(volumes),
        "count": len(volumes),
    }
