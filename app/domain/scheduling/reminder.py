"""Whether a training reminder should fire today."""

from datetime import date

def should_remind(*, last_trained: date | None, today: date | None = None, gap_days: int = 2) -> bool:
    day = today or date.today()
    if last_trained is None:
        return True
    return (day - last_trained).days >= gap_days
