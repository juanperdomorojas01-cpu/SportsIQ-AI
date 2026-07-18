from decimal import Decimal

from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel
from app.models.enums import BetResult
from app.models.enums import BetStatus


class Bet(BaseModel):
    __tablename__ = "bets"

    bankroll_id: Mapped[int] = mapped_column(
        ForeignKey("bankrolls.id"),
        nullable=False,
    )

    fixture_id: Mapped[int] = mapped_column(
        ForeignKey("fixtures.id"),
        nullable=False,
    )

    bookmaker_id: Mapped[int] = mapped_column(
        ForeignKey("bookmakers.id"),
        nullable=False,
    )

    market_id: Mapped[int] = mapped_column(
        ForeignKey("bet_markets.id"),
        nullable=False,
    )

    bet_type_id: Mapped[int] = mapped_column(
        ForeignKey("bet_types.id"),
        nullable=False,
    )

    selection: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    stake: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    odds: Mapped[Decimal] = mapped_column(
        Numeric(8, 2),
        nullable=False,
    )

    potential_return: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    payout: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True,
    )

    profit: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True,
    )

    status: Mapped[BetStatus] = mapped_column(
        Enum(BetStatus),
        default=BetStatus.PENDING,
        nullable=False,
    )

    result: Mapped[BetResult | None] = mapped_column(
        Enum(BetResult),
        nullable=True,
    )

    placed_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    settled_at: Mapped[DateTime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    bankroll = relationship(
        "Bankroll",
        back_populates="bets",
    )

    bookmaker = relationship(
        "Bookmaker",
        back_populates="bets",
    )

    fixture = relationship(
        "Fixture",
    )

    market = relationship(
        "BetMarket",
        back_populates="bets",
    )

    bet_type = relationship(
        "BetType",
        back_populates="bets",
    )

    transactions = relationship(
        "Transaction",
        back_populates="bet",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return (
            f"<Bet("
            f"id={self.id}, "
            f"fixture_id={self.fixture_id}, "
            f"stake={self.stake}, "
            f"odds={self.odds}, "
            f"status='{self.status.value}'"
            f")>"
        )