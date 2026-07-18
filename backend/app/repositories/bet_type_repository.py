from sqlalchemy.orm import Session

from app.models.bet_type import BetType


class BetTypeRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, bet_type_id: int) -> BetType | None:
        return (
            self.db.query(BetType)
            .filter(BetType.id == bet_type_id)
            .first()
        )

    def get_all(self) -> list[BetType]:
        return (
            self.db.query(BetType)
            .order_by(BetType.name)
            .all()
        )

    def create(self, bet_type: BetType) -> BetType:
        self.db.add(bet_type)
        self.db.flush()
        self.db.refresh(bet_type)
        return bet_type