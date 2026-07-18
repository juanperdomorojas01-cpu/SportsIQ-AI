from datetime import datetime

from app.models.enums import AccountStatus
from app.models.user import User

from app.repositories.role_repository import RoleRepository
from app.repositories.user_repository import UserRepository

from app.schemas.user import UserCreate

from app.security.jwt import create_access_token
from app.security.password import hash_password
from app.security.password import verify_password


class AuthService:

    def __init__(
        self,
        user_repository: UserRepository,
        role_repository: RoleRepository,
    ):
        self.user_repository = user_repository
        self.role_repository = role_repository

    # ==========================
    # Authentication
    # ==========================

    def register(self, data: UserCreate) -> User:

        if self.user_repository.get_by_email(data.email):
            raise ValueError("El correo ya está registrado.")

        if self.user_repository.get_by_username(data.username):
            raise ValueError("El nombre de usuario ya está registrado.")

        role = self.role_repository.get_by_name("USER")

        if role is None:
            raise ValueError("No existe el rol USER.")

        user = User(
            email=data.email,
            username=data.username,
            hashed_password=hash_password(data.password),
            first_name=data.first_name,
            last_name=data.last_name,
            status=AccountStatus.PENDING,
            role_id=role.id,
        )

        return self.user_repository.create(user)

    def login(self, username: str, password: str) -> str:

        user = self.user_repository.get_by_username(username)

        if user is None:
            raise ValueError("Usuario o contraseña incorrectos.")

        if not verify_password(password, user.hashed_password):
            raise ValueError("Usuario o contraseña incorrectos.")

        if user.status != AccountStatus.ACTIVE:
            raise ValueError(
                "La cuenta aún no está activa."
            )

        user.last_login = datetime.utcnow()
        self.user_repository.update(user)

        return create_access_token(
            {
                "sub": str(user.id),
                "email": user.email,
                "role": user.role.name,
            }
        )

    # ==========================
    # User Administration
    # ==========================

    def get_users(self) -> list[User]:
        return self.user_repository.get_all()

    def get_user(self, user_id: int) -> User:

        user = self.user_repository.get_by_id(user_id)

        if user is None:
            raise ValueError("Usuario no encontrado.")

        return user

    def activate_user(self, user_id: int) -> User:

        user = self.get_user(user_id)

        user.status = AccountStatus.ACTIVE

        return self.user_repository.update(user)

    def suspend_user(self, user_id: int) -> User:

        user = self.get_user(user_id)

        user.status = AccountStatus.SUSPENDED

        return self.user_repository.update(user)

    def change_role(
        self,
        user_id: int,
        role_name: str,
    ) -> User:

        user = self.get_user(user_id)

        role = self.role_repository.get_by_name(role_name)

        if role is None:
            raise ValueError("El rol no existe.")

        user.role_id = role.id

        return self.user_repository.update(user)