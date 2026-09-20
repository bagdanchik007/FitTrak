from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database.base import Base, SoftDeleteMixin, TimestampMixin, UUIDPrimaryKeyMixin


class WorkoutTemplateModel(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "workout_templates"

    user_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    items = relationship(
        "WorkoutTemplateItemModel",
        back_populates="template",
        cascade="all, delete-orphan",
        lazy="selectin",
    )


class WorkoutTemplateItemModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "workout_template_items"

    template_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("workout_templates.id", ondelete="CASCADE"), nullable=False, index=True
    )
    exercise_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("exercises.id", ondelete="RESTRICT"), nullable=False
    )
    target_sets: Mapped[int] = mapped_column(Integer, nullable=False, default=3)
    target_reps: Mapped[int | None] = mapped_column(Integer, nullable=True)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    template = relationship("WorkoutTemplateModel", back_populates="items")
