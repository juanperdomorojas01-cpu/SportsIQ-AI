from sqlalchemy.orm import Session

from app.models.transaction import Transaction
from app.repositories.base_repository import BaseRepository


class TransactionRepository(BaseRepository[Transaction]):
    model = Transaction

    def __init__(self, db: Session):
        super().__init__(db)

    def get_by_bankroll(self, bankroll_id: int) -> list[Transaction]:
        return (
            self.db.query(Transaction)
            .filter(Transaction.bankroll_id == bankroll_id)
            .order_by(Transaction.created_at.desc())
            .all()
        )

    def get_by_bet(self, bet_id: int) -> list[Transaction]:
        return (
            self.db.query(Transaction)
            .filter(Transaction.bet_id == bet_id)
            .order_by(Transaction.created_at.desc())
            .all()
        )