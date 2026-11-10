from app.domain.math_util.percent import percent_of
from app.domain.color.tone import progress_tone

def progress_view(current: float, target: float) -> dict:
    pct = percent_of(current=current, target=target)
    return {"percent": pct, "tone": progress_tone(pct), "current": current, "target": target}
