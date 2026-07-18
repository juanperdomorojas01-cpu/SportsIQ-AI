from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from app.core.dependencies import get_current_user
from app.models.user import User


def require_role(role_name: str):

    def dependency(
        current_user: User = Depends(get_current_user),
    ):

        if current_user.role is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="El usuario no tiene un rol asignado.",
            )

        if current_user.role.name != role_name:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No tienes permisos para acceder a este recurso.",
            )

        return current_user

    return dependency


require_admin = require_role("ADMIN")
require_user = require_role("USER")