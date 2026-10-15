"""Email delivery: SMTP when configured, otherwise structured log (dev-safe)."""

from __future__ import annotations

import logging
import smtplib
from email.message import EmailMessage

from app.core.config import get_settings

logger = logging.getLogger("fittrack.mail")


def send_email(*, to: str, subject: str, body: str) -> dict:
    """Send an email or log it when SMTP is not configured.

    Returns a status dict suitable for API responses / tests.
    """
    settings = get_settings()
    if not settings.smtp_host:
        logger.info("email_dev_mode to=%s subject=%s body=%s", to, subject, body[:200])
        return {"status": "logged", "to": to, "subject": subject, "delivery": "dev_log"}

    msg = EmailMessage()
    msg["From"] = settings.smtp_from
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP(settings.smtp_host, settings.smtp_port, timeout=15) as smtp:
            if settings.smtp_tls:
                smtp.starttls()
            if settings.smtp_user and settings.smtp_password:
                smtp.login(settings.smtp_user, settings.smtp_password)
            smtp.send_message(msg)
        return {"status": "sent", "to": to, "subject": subject, "delivery": "smtp"}
    except OSError as exc:
        logger.exception("smtp_failed")
        return {"status": "error", "to": to, "detail": str(exc), "delivery": "smtp"}


def send_verification_email(*, to: str, token: str) -> dict:
    subject = "Verify your FitTrack email"
    body = (
        "Welcome to FitTrack.\n\n"
        f"Your verification token: {token}\n\n"
        "Call POST /api/v1/auth/verify-email with this token, "
        "or open your app verification screen.\n"
    )
    return send_email(to=to, subject=subject, body=body)
