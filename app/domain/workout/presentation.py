"""UI-oriented workout helpers."""


def empty_workout_list_message(*, can_create: bool = True) -> str:
    if can_create:
        return "No workouts yet — log your first session."
    return "No workouts found."
