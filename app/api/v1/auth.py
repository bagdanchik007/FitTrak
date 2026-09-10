from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.services.auth_service import AuthService
from app.core.dependencies import DbSession
from app.infrastructure.repositories.user_repository import SQLAlchemyUserRepository
from app.schemas.user import Token, UserCreate, UserRead

router = APIRouter(prefix="/auth", tags=["Authentication"])


def get_auth_service(db: DbSession) -> AuthService:
    return AuthService(user_repo=SQLAlchemyUserRepository(db))


@router.post(
    "/register",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
)
async def register(
    data: UserCreate,
    service: AuthService = Depends(get_auth_service),
) -> UserRead:
    return await service.register(data)


@router.post(
    "/login",
    response_model=Token,
    summary="Login and receive access + refresh tokens",
)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: AuthService = Depends(get_auth_service),
) -> Token:
    return await service.login(email=form_data.username, password=form_data.password)
