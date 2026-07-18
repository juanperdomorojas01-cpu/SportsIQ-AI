from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr

from app.models.enums import AccountStatus


class RoleResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str
    first_name: str
    last_name: str


class UserResponse(BaseModel):
    id: int

    email: EmailStr
    username: str

    first_name: str
    last_name: str

    status: AccountStatus

    subscription_start: datetime | None
    subscription_end: datetime | None
    last_login: datetime | None

    role: RoleResponse

    model_config = ConfigDict(from_attributes=True)