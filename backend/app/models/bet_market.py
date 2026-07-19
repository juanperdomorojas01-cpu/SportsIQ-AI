from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel


class BetMarket(BaseModel):
    __tablename__ = "bet_markets"

    api_id: Mapped[int] = mapped_column(
        Integer,
        unique=True,
        index=True,
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    bets = relationship(
        "Bet",
        back_populates="market",
    )

    def __repr__(self) -> str:
        return (
            f"<BetMarket("
            f"id={self.id}, "
            f"api_id={self.api_id}, "
            f"name='{self.name}'"
            f")>"
        )