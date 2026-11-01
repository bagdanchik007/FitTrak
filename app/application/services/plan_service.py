from app.domain.plan.split import next_split_day

def suggest_next_day(last_focus: str | None = None) -> dict:
    focus = next_split_day(last_focus)
    return {"focus": focus, "label": focus.replace("_", " ").title()}
