from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.services.auth_service import AuthService
from app.core.dependencies import DbSession
from app.infrastructure.repositories.user_repository import SQLAlchemyUserRepository
from app.schemas.user import PasswordChange, RefreshTokenRequest, Token, UserCreate, UserRead
from app.core.dependencies import CurrentUserId
from app.core.rate_limit import rate_limit

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
    _: None = Depends(rate_limit(max_requests=20, window_seconds=60)),
) -> Token:
    return await service.login(email=form_data.username, password=form_data.password)


@router.post(
    "/refresh",
    response_model=Token,
    summary="Refresh access token using refresh token",
)
async def refresh_token(
    body: RefreshTokenRequest,
    service: AuthService = Depends(get_auth_service),
) -> Token:
    return await service.refresh(body.refresh_token)


@router.post(
    "/change-password",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Change password for current user",
)
async def change_password(
    body: PasswordChange,
    user_id: CurrentUserId,
    service: AuthService = Depends(get_auth_service),
    _: None = Depends(rate_limit(max_requests=10, window_seconds=60)),
) -> None:
    await service.change_password(user_id, body.current_password, body.new_password)


@router.post(
    "/logout",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Logout (client should discard tokens)",
)
async def logout() -> None:
    """Stateless JWT logout – client discards tokens. Server-side blacklist can be added later."""
    return None

