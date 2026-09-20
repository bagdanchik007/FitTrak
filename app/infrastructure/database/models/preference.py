from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class UserPreferenceModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "user_preferences"

    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False
    )
    weight_unit: Mapped[str] = mapped_column(String(10), default="kg", nullable=False)
    language: Mapped[str] = mapped_column(String(10), default="en", nullable=False)
    weekly_goal_workouts: Mapped[int] = mapped_column(Integer, default=3, nullable=False)
    email_reminders: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
