from sqlalchemy.orm import Session

from app.models.bet import Bet
from app.models.enums import BetStatus
from app.repositories.base_repository import BaseRepository


class BetRepository(BaseRepository[Bet]):
    model = Bet

    def __init__(self, db: Session):
        super().__init__(db)

    def get_by_bankroll(self, bankroll_id: int) -> list[Bet]:
        return (
            self.db.query(Bet)
            .filter(Bet.bankroll_id == bankroll_id)
            .order_by(Bet.placed_at.desc())
            .all()
        )

    def get_pending(self, bankroll_id: int) -> list[Bet]:
        return (
            self.db.query(Bet)
            .filter(
                Bet.bankroll_id == bankroll_id,
                Bet.status == BetStatus.PENDING,
            )
            .order_by(Bet.placed_at.desc())
            .all()
        )