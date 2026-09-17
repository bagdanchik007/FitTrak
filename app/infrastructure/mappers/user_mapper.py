"""Map between UserModel and User entity."""

from app.domain.user.entities import User
from app.infrastructure.database.models.user import UserModel


def model_to_user(model: UserModel) -> User:
    return User(
        id=model.id,
        email=model.email,
        hashed_password=model.hashed_password,
        full_name=model.full_name,
        is_active=model.is_active,
        is_superuser=model.is_superuser,
        created_at=model.created_at,
        updated_at=model.updated_at,
        last_login_at=model.last_login_at,
        deleted_at=model.deleted_at,
    )


def user_to_model_data(user: User) -> dict:
    return {
        "id": user.id,
        "email": user.email.lower(),
        "hashed_password": user.hashed_password,
        "full_name": user.full_name,
        "is_active": user.is_active,
        "is_superuser": user.is_superuser,
        "last_login_at": user.last_login_at,
    }
