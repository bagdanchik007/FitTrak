"""Database helper utilities."""

from sqlalchemy import Select
from sqlalchemy.sql import func


def apply_pagination(stmt: Select, skip: int, limit: int) -> Select:
    return stmt.offset(skip).limit(limit)


async def count_stmt(session, base_stmt: Select) -> int:
    result = await session.execute(select_count(base_stmt))
    return int(result.scalar() or 0)


def select_count(base_stmt: Select):
    return func.count().select_from(base_stmt.order_by(None).subquery())
