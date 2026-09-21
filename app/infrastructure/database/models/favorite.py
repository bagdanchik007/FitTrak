from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class ExerciseFavoriteModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "exercise_favorites"
    __table_args__ = (
        UniqueConstraint("user_id", "exercise_id", name="uq_user_exercise_favorite"),
    )

    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    exercise_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("exercises.id", ondelete="CASCADE"), nullable=False, index=True
    )
