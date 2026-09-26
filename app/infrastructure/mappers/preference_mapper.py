from app.domain.preference.entities import UserPreference
from app.infrastructure.database.models.preference import UserPreferenceModel


def model_to_preference(model: UserPreferenceModel) -> UserPreference:
    return UserPreference(
        id=model.id,
        user_id=model.user_id,
        weight_unit=model.weight_unit,
        language=model.language,
        weekly_goal_workouts=model.weekly_goal_workouts,
        email_reminders=model.email_reminders,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )
