from app.domain.ai.prompt_safety import sanitize_coach_message

def test_sanitize():
    assert len(sanitize_coach_message("  hi  " * 1000, max_len=20)) <= 20
