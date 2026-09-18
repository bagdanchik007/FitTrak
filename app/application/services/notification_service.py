"""Placeholder notification service (email/push later)."""

from app.core.logging import get_logger

logger = get_logger(__name__)


class NotificationService:
    async def send_welcome(self, email: str) -> None:
        logger.info("welcome_notification_queued", email=email)

    async def send_password_changed(self, email: str) -> None:
        logger.info("password_changed_notification_queued", email=email)
