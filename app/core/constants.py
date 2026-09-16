"""Application-wide constants."""

# Pagination
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100

# Token types
TOKEN_TYPE_ACCESS = "access"
TOKEN_TYPE_REFRESH = "refresh"

# Muscle groups (common values for validation / filtering)
MUSCLE_GROUPS = [
    "chest",
    "back",
    "shoulders",
    "biceps",
    "triceps",
    "legs",
    "core",
    "glutes",
    "full_body",
    "cardio",
]

# Equipment types
EQUIPMENT_TYPES = [
    "barbell",
    "dumbbell",
    "machine",
    "cable",
    "bodyweight",
    "kettlebell",
    "resistance_band",
    "other",
]

# HTTP related
API_VERSION = "v1"

# API may accept free-text muscle_group; constants list is for UI suggestions
