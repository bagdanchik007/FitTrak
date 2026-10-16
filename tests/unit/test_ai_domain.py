from app.domain.ai.services import coach_reply, suggest_focus, suggest_session

def test_suggest_focus_rotation():
    assert suggest_focus(recent_focuses=["push", "pull"]) == "legs"

def test_suggest_session():
    s = suggest_session(focus="push", experience="beginner")
    assert s["focus"] == "push"
    assert s["exercises"]

def test_coach_reply_beginner():
    r = coach_reply("I am a beginner")
    assert "full-body" in r.lower() or "week" in r.lower()
