from decimal import Decimal

from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel


class Bankroll(BaseModel):
    __tablename__ = "bankrolls"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
        nullable=False,
    )

    initial_balance: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    current_balance: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    currency: Mapped[str] = mapped_column(
        String(10),
        default="USD",
        nullable=False,
    )

    total_profit: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        default=Decimal("0.00"),
        nullable=False,
    )

    total_loss: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        default=Decimal("0.00"),
        nullable=False,
    )

    user = relationship(
        "User",
        back_populates="bankroll",
    )

    bets = relationship(
        "Bet",
        back_populates="bankroll",
        cascade="all, delete-orphan",
    )

    transactions = relationship(
        "Transaction",
        back_populates="bankroll",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return (
            f"<Bankroll("
            f"id={self.id}, "
            f"user_id={self.user_id}, "
            f"balance={self.current_balance}"
            f")>"
        )