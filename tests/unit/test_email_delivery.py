from app.application.services.email_delivery_service import send_email, send_verification_email

def test_send_email_dev_log(monkeypatch):
    class S:
        smtp_host = None
        smtp_from = "x@y.z"
    monkeypatch.setattr("app.application.services.email_delivery_service.get_settings", lambda: S())
    result = send_email(to="a@b.c", subject="Hi", body="Body")
    assert result["status"] == "logged"
    assert result["delivery"] == "dev_log"

def test_send_verification_email(monkeypatch):
    class S:
        smtp_host = None
        smtp_from = "x@y.z"
    monkeypatch.setattr("app.application.services.email_delivery_service.get_settings", lambda: S())
    result = send_verification_email(to="a@b.c", token="tok123")
    assert result["status"] == "logged"
