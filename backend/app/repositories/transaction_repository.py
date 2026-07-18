from sqlalchemy import select

from app.models.transaction import Transaction
from app.repositories.base_repository import BaseRepository


class TransactionRepository(BaseRepository[Transaction]):

    def __init__(self, db):
        super().__init__(db, Transaction)

    def get_by_bankroll(self, bankroll_id: int) -> list[Transaction]:

        stmt = (
            select(Transaction)
            .where(Transaction.bankroll_id == bankroll_id)
            .order_by(Transaction.created_at.desc())
        )

        return list(self.scalars(stmt))

    def get_by_bet(self, bet_id: int) -> list[Transaction]:

        stmt = (
            select(Transaction)
            .where(Transaction.bet_id == bet_id)
            .order_by(Transaction.created_at.desc())
        )

        return list(self.scalars(stmt))