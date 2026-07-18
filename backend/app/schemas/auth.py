from datetime import datetime

from pydantic import BaseModel, EmailStr

from app.models.enums import AccountStatus


class LoginRequest(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class CurrentUser(BaseModel):
    id: int
    email: EmailStr
    username: str
    first_name: str
    last_name: str
    status: AccountStatus
    subscription_start: datetime | None
    subscription_end: datetime | None
    last_login: datetime | None
    role: str