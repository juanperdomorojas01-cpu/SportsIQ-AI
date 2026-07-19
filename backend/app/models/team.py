from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.league import League


class Team(Base):
    __tablename__ = "teams"

    id: Mapped[int] = mapped_column(primary_key=True)

    api_id: Mapped[int] = mapped_column(unique=True, index=True)

    name: Mapped[str] = mapped_column(String(150))

    code: Mapped[str | None] = mapped_column(
        String(10),
        nullable=True
    )

    country: Mapped[str] = mapped_column(String(100))

    founded: Mapped[int | None] = mapped_column(nullable=True)

    national: Mapped[bool]

    logo: Mapped[str] = mapped_column(String(500))

    league_id: Mapped[int | None] = mapped_column(
        ForeignKey("leagues.id"),
        nullable=True
    )

    league: Mapped["League"] = relationship(
        back_populates="teams"
    )

    players = relationship(
    "Player",
    back_populates="team",
    cascade="all, delete-orphan",
)