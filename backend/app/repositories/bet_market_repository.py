from sqlalchemy.orm import Session

from app.models.bet_market import BetMarket


class BetMarketRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, market_id: int) -> BetMarket | None:
        return (
            self.db.query(BetMarket)
            .filter(BetMarket.id == market_id)
            .first()
        )

    def get_all(self) -> list[BetMarket]:
        return (
            self.db.query(BetMarket)
            .order_by(BetMarket.name)
            .all()
        )

    def create(self, market: BetMarket) -> BetMarket:
        self.db.add(market)
        self.db.flush()
        self.db.refresh(market)
        return market