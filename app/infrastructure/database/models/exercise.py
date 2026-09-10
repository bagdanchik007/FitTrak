from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database.base import Base, SoftDeleteMixin, TimestampMixin, UUIDPrimaryKeyMixin


class ExerciseModel(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "exercises"

    name: Mapped[str] = mapped_column(String(120), nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    muscle_group: Mapped[str | None] = mapped_column(String(80), nullable=True, index=True)
    equipment: Mapped[str | None] = mapped_column(String(80), nullable=True)

    # Owner (null = system/default exercise)
    created_by: Mapped[UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
    )

    created_by_user = relationship("UserModel", back_populates="exercises")
    sets = relationship("WorkoutSetModel", back_populates="exercise", lazy="selectin")
