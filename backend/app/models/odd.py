from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel


class Odd(BaseModel):
    __tablename__ = "odds"

    __table_args__ = (
        UniqueConstraint(
            "fixture_id",
            "bookmaker_id",
            "bet_type_id",
            name="uq_odds_fixture_bookmaker_bettype",
        ),
    )

    fixture_id: Mapped[int] = mapped_column(
        ForeignKey("fixtures.id"),
        nullable=False,
        index=True,
    )

    bookmaker_id: Mapped[int] = mapped_column(
        ForeignKey("bookmakers.id"),
        nullable=False,
        index=True,
    )

    bet_type_id: Mapped[int] = mapped_column(
        ForeignKey("bet_types.id"),
        nullable=False,
        index=True,
    )

    updated_at_api: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    fixture = relationship(
        "Fixture",
        back_populates="odds",
    )

    bookmaker = relationship(
        "Bookmaker",
        back_populates="odds",
    )

    bet_type = relationship(
        "BetType",
        back_populates="odds",
    )

    values = relationship(
        "OddValue",
        back_populates="odd",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return (
            f"<Odd("
            f"id={self.id}, "
            f"fixture_id={self.fixture_id}, "
            f"bookmaker_id={self.bookmaker_id}, "
            f"bet_type_id={self.bet_type_id}"
            f")>"
        )