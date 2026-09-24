from datetime import date

from pydantic import BaseModel


class ActivityItem(BaseModel):
    type: str
    title: str
    occurred_on: date
    meta: dict | None = None
