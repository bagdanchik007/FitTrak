from app.domain.workout.presentation import empty_workout_list_message

def test_empty_message():
    assert "log" in empty_workout_list_message().lower()
