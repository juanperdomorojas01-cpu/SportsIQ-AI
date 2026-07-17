from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Fixture(Base):
    __tablename__ = "fixtures"

    id: Mapped[int] = mapped_column(primary_key=True)

    api_id: Mapped[int] = mapped_column(
        unique=True,
        index=True
    )

    referee: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True
    )

    timezone: Mapped[str] = mapped_column(
        String(50)
    )

    date: Mapped[datetime] = mapped_column(
        DateTime
    )

    timestamp: Mapped[int]

    status: Mapped[str] = mapped_column(
        String(30)
    )

    league_id: Mapped[int] = mapped_column(
        ForeignKey("leagues.id"),
        nullable=False
    )

    home_team_id: Mapped[int] = mapped_column(
        ForeignKey("teams.id"),
        nullable=False
    )

    away_team_id: Mapped[int] = mapped_column(
        ForeignKey("teams.id"),
        nullable=False
    )

    home_goals: Mapped[int | None] = mapped_column(
        nullable=True
    )

    away_goals: Mapped[int | None] = mapped_column(
        nullable=True
    )