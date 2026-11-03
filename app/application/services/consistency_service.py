from app.domain.consistency.band import consistency_band

def band_payload(score: float | None) -> dict:
    return {"score": score, "band": consistency_band(score)}
