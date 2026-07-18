from sqlalchemy import select

from app.models.bankroll import Bankroll
from app.repositories.base_repository import BaseRepository


class BankrollRepository(BaseRepository[Bankroll]):

    def __init__(self, db):
        super().__init__(db, Bankroll)

    def get_by_user_id(self, user_id: int) -> Bankroll | None:

        stmt = (
            select(Bankroll)
            .where(Bankroll.user_id == user_id)
        )

        return self.scalar(stmt)