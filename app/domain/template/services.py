"""Template domain helpers."""

from app.domain.template.entities import TemplateItem, WorkoutTemplate


def total_target_sets(template: WorkoutTemplate) -> int:
    return sum(item.target_sets for item in template.items)


def sorted_items(template: WorkoutTemplate) -> list[TemplateItem]:
    return sorted(template.items, key=lambda i: i.sort_order)
