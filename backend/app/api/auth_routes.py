from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.core.permissions import require_admin

from app.db.database import get_db

from app.models.user import User

from app.repositories.role_repository import RoleRepository
from app.repositories.user_repository import UserRepository

from app.schemas.admin import ChangeRoleRequest
from app.schemas.auth import CurrentUser
from app.schemas.auth import Token
from app.schemas.user import UserCreate
from app.schemas.user import UserResponse

from app.services.auth_service import AuthService


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


def get_auth_service(
    db: Session = Depends(get_db),
) -> AuthService:
    return AuthService(
        UserRepository(db),
        RoleRepository(db),
    )


# ==========================================================
# Authentication
# ==========================================================

@router.post(
    "/register",
    response_model=UserResponse,
)
def register(
    data: UserCreate,
    service: AuthService = Depends(get_auth_service),
):
    try:
        return service.register(data)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.post(
    "/login",
    response_model=Token,
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: AuthService = Depends(get_auth_service),
):
    try:
        token = service.login(
            form_data.username,
            form_data.password,
        )

        return Token(
            access_token=token,
            token_type="bearer",
        )

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e),
        )


@router.get(
    "/me",
    response_model=CurrentUser,
)
def me(
    current_user: User = Depends(get_current_user),
):

    return CurrentUser(
        id=current_user.id,
        email=current_user.email,
        username=current_user.username,
        first_name=current_user.first_name,
        last_name=current_user.last_name,
        status=current_user.status,
        subscription_start=current_user.subscription_start,
        subscription_end=current_user.subscription_end,
        last_login=current_user.last_login,
        role=current_user.role.name,
    )


# ==========================================================
# Administration
# ==========================================================

@router.get(
    "/users",
    response_model=list[UserResponse],
)
def get_users(
    service: AuthService = Depends(get_auth_service),
    _: User = Depends(require_admin),
):
    return service.get_users()


@router.get(
    "/users/{user_id}",
    response_model=UserResponse,
)
def get_user(
    user_id: int,
    service: AuthService = Depends(get_auth_service),
    _: User = Depends(require_admin),
):
    try:
        return service.get_user(user_id)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.patch(
    "/users/{user_id}/activate",
    response_model=UserResponse,
)
def activate_user(
    user_id: int,
    service: AuthService = Depends(get_auth_service),
    _: User = Depends(require_admin),
):
    try:
        return service.activate_user(user_id)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.patch(
    "/users/{user_id}/suspend",
    response_model=UserResponse,
)
def suspend_user(
    user_id: int,
    service: AuthService = Depends(get_auth_service),
    _: User = Depends(require_admin),
):
    try:
        return service.suspend_user(user_id)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.patch(
    "/users/{user_id}/role",
    response_model=UserResponse,
)
def change_role(
    user_id: int,
    data: ChangeRoleRequest,
    service: AuthService = Depends(get_auth_service),
    _: User = Depends(require_admin),
):
    try:
        return service.change_role(
            user_id,
            data.role,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )