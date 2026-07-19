from sqlalchemy.orm import Session

from app.models.bankroll import Bankroll
from app.repositories.base_repository import BaseRepository


class BankrollRepository(BaseRepository[Bankroll]):
    model = Bankroll

    def __init__(self, db: Session):
        super().__init__(db)

    def get_by_user_id(self, user_id: int) -> Bankroll | None:
        return (
            self.db.query(Bankroll)
            .filter(Bankroll.user_id == user_id)
            .first()
        )