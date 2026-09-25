"""Template application helpers."""

from app.domain.template.entities import WorkoutTemplate
from app.domain.template.services import sorted_items, total_target_sets


def template_overview(template: WorkoutTemplate) -> dict:
    return {
        "name": template.name,
        "item_count": len(template.items),
        "total_target_sets": total_target_sets(template),
        "ordered_exercise_ids": [i.exercise_id for i in sorted_items(template)],
    }
