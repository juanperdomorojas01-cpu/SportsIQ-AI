from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Standing(Base):
    __tablename__ = "standings"

    id: Mapped[int] = mapped_column(primary_key=True)

    league_id: Mapped[int] = mapped_column(
        ForeignKey("leagues.id"),
        nullable=False
    )

    team_id: Mapped[int] = mapped_column(
        ForeignKey("teams.id"),
        nullable=False
    )

    season: Mapped[int]

    position: Mapped[int]

    points: Mapped[int]

    played: Mapped[int]

    win: Mapped[int]

    draw: Mapped[int]

    lose: Mapped[int]

    goals_for: Mapped[int]

    goals_against: Mapped[int]

    goal_difference: Mapped[int]

    form: Mapped[str | None] = mapped_column(nullable=True)