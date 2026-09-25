from app.domain.template.entities import TemplateItem, WorkoutTemplate
from app.infrastructure.database.models.template import WorkoutTemplateItemModel, WorkoutTemplateModel


def model_to_template(model: WorkoutTemplateModel) -> WorkoutTemplate:
    items = [
        TemplateItem(
            id=i.id,
            template_id=i.template_id,
            exercise_id=i.exercise_id,
            target_sets=i.target_sets,
            target_reps=i.target_reps,
            sort_order=i.sort_order,
        )
        for i in (model.items or [])
    ]
    return WorkoutTemplate(
        id=model.id,
        user_id=model.user_id,
        name=model.name,
        description=model.description,
        created_at=model.created_at,
        updated_at=model.updated_at,
        items=items,
        deleted_at=model.deleted_at,
    )


def model_to_template_item(model: WorkoutTemplateItemModel) -> TemplateItem:
    return TemplateItem(
        id=model.id,
        template_id=model.template_id,
        exercise_id=model.exercise_id,
        target_sets=model.target_sets,
        target_reps=model.target_reps,
        sort_order=model.sort_order,
    )
