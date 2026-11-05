from app.domain.live.status import live_status_label

def status_payload(status: str | None) -> dict:
    return {"status": status, "label": live_status_label(status)}
