from pydantic import BaseModel


class ChangeRoleRequest(BaseModel):
    role: str