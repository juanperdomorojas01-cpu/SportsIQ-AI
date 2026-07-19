from sqlalchemy.orm import Session

from app.models.role import Role
from app.repositories.base_repository import BaseRepository


class RoleRepository(BaseRepository[Role]):
    model = Role

    def __init__(self, db: Session):
        super().__init__(db)

    def get_by_id(self, role_id: int) -> Role | None:
        return (
            self.db.query(Role)
            .filter(Role.id == role_id)
            .first()
        )

    def get_by_name(self, name: str) -> Role | None:
        return (
            self.db.query(Role)
            .filter(Role.name == name)
            .first()
        )

    def get_all(self) -> list[Role]:
        return (
            self.db.query(Role)
            .order_by(Role.id)
            .all()
        )

    def create(self, role: Role) -> Role:
        self.db.add(role)
        self.db.commit()
        self.db.refresh(role)
        return role

    def update(self, role: Role) -> Role:
        self.db.commit()
        self.db.refresh(role)
        return role

    def delete(self, role: Role) -> None:
        self.db.delete(role)
        self.db.commit()