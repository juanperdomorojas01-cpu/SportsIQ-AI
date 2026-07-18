from sqlalchemy import select

from app.models.bet import Bet
from app.models.enums import BetStatus
from app.repositories.base_repository import BaseRepository


class BetRepository(BaseRepository[Bet]):

    def __init__(self, db):
        super().__init__(db, Bet)

    def get_by_bankroll(self, bankroll_id: int) -> list[Bet]:

        stmt = (
            select(Bet)
            .where(Bet.bankroll_id == bankroll_id)
            .order_by(Bet.placed_at.desc())
        )

        return list(self.scalars(stmt))

    def get_pending(self, bankroll_id: int) -> list[Bet]:

        stmt = (
            select(Bet)
            .where(
                Bet.bankroll_id == bankroll_id,
                Bet.status == BetStatus.PENDING,
            )
            .order_by(Bet.placed_at.desc())
        )

        return list(self.scalars(stmt))