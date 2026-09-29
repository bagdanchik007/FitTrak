"""composite index workouts user_id performed_at

Revision ID: 004
Revises: 003
Create Date: 2026-10-19
"""
from typing import Sequence, Union

from alembic import op

revision: str = "004"
down_revision: Union[str, None] = "003"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_index(
        "ix_workouts_user_performed_at",
        "workouts",
        ["user_id", "performed_at"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index("ix_workouts_user_performed_at", table_name="workouts")
