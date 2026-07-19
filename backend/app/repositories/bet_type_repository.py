from sqlalchemy.orm import Session

from app.models.bet_type import BetType
from app.repositories.base_repository import BaseRepository


class BetTypeRepository(BaseRepository[BetType]):
    model = BetType

    def __init__(self, db: Session):
        super().__init__(db)

    def get_by_api_id(self, api_id: int) -> BetType | None:
        return (
            self.db.query(BetType)
            .filter(BetType.api_id == api_id)
            .first()
        )

    def get_by_name(self, name: str) -> BetType | None:
        return (
            self.db.query(BetType)
            .filter(BetType.name == name)
            .first()
        )

    def get_all(self) -> list[BetType]:
        return (
            self.db.query(BetType)
            .order_by(BetType.name)
            .all()
        )

    def count(self) -> int:
        return self.db.query(BetType).count()