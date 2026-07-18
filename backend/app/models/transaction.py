from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel
from app.models.enums import TransactionType


class Transaction(BaseModel):
    __tablename__ = "transactions"

    bankroll_id: Mapped[int] = mapped_column(
        ForeignKey("bankrolls.id"),
        nullable=False,
    )

    bet_id: Mapped[int | None] = mapped_column(
        ForeignKey("bets.id"),
        nullable=True,
    )

    type: Mapped[TransactionType] = mapped_column(
        Enum(TransactionType),
        nullable=False,
    )

    amount: Mapped[float] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    balance_before: Mapped[float] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    balance_after: Mapped[float] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    bankroll = relationship(
        "Bankroll",
        back_populates="transactions",
    )

    bet = relationship(
        "Bet",
        back_populates="transactions",
    )