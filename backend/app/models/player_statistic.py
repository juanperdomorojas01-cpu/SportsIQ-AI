from sqlalchemy import (
    Boolean,
    Float,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class PlayerStatistic(BaseModel):
    __tablename__ = "player_statistics"

    __table_args__ = (
        UniqueConstraint(
            "player_id",
            "team_id",
            "league_id",
            "season",
            name="uq_player_statistics",
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    player_id: Mapped[int] = mapped_column(
        ForeignKey(
            "players.id",
            ondelete="CASCADE",
        )
    )

    team_id: Mapped[int] = mapped_column(
        ForeignKey(
            "teams.id",
            ondelete="CASCADE",
        )
    )

    league_id: Mapped[int] = mapped_column(
        ForeignKey(
            "leagues.id",
            ondelete="CASCADE",
        )
    )

    season: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    # ==================================================
    # Games
    # ==================================================

    appearances: Mapped[int | None] = mapped_column(Integer, nullable=True)
    lineups: Mapped[int | None] = mapped_column(Integer, nullable=True)
    minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    number: Mapped[int | None] = mapped_column(Integer, nullable=True)
    position: Mapped[str | None] = mapped_column(String(50), nullable=True)
    rating: Mapped[float | None] = mapped_column(Float, nullable=True)
    captain: Mapped[bool] = mapped_column(Boolean, default=False)

    # ==================================================
    # Substitutes
    # ==================================================

    sub_in: Mapped[int | None] = mapped_column(Integer, nullable=True)
    sub_out: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bench: Mapped[int | None] = mapped_column(Integer, nullable=True)

    # ==================================================
    # Shots
    # ==================================================

    shots_total: Mapped[int | None] = mapped_column(Integer, nullable=True)
    shots_on: Mapped[int | None] = mapped_column(Integer, nullable=True)

    # ==================================================
    # Goals
    # ==================================================

    goals: Mapped[int | None] = mapped_column(Integer, nullable=True)
    assists: Mapped[int | None] = mapped_column(Integer, nullable=True)
    goals_conceded: Mapped[int | None] = mapped_column(Integer, nullable=True)
    saves: Mapped[int | None] = mapped_column(Integer, nullable=True)

    # ==================================================
    # Passes
    # ==================================================

    passes_total: Mapped[int | None] = mapped_column(Integer, nullable=True)
    passes_key: Mapped[int | None] = mapped_column(Integer, nullable=True)
    passes_accuracy: Mapped[int | None] = mapped_column(Integer, nullable=True)

    # ==================================================
    # Tackles
    # ==================================================

    tackles_total: Mapped[int | None] = mapped_column(Integer, nullable=True)
    blocks: Mapped[int | None] = mapped_column(Integer, nullable=True)
    interceptions: Mapped[int | None] = mapped_column(Integer, nullable=True)

    # ==================================================
    # Duels
    # ==================================================

    duels_total: Mapped[int | None] = mapped_column(Integer, nullable=True)
    duels_won: Mapped[int | None] = mapped_column(Integer, nullable=True)

    # ==================================================
    # Dribbles
    # ==================================================

    dribbles_attempts: Mapped[int | None] = mapped_column(Integer, nullable=True)
    dribbles_success: Mapped[int | None] = mapped_column(Integer, nullable=True)
    dribbled_past: Mapped[int | None] = mapped_column(Integer, nullable=True)

    # ==================================================
    # Fouls
    # ==================================================

    fouls_drawn: Mapped[int | None] = mapped_column(Integer, nullable=True)
    fouls_committed: Mapped[int | None] = mapped_column(Integer, nullable=True)

    # ==================================================
    # Cards
    # ==================================================

    yellow: Mapped[int | None] = mapped_column(Integer, nullable=True)
    yellow_red: Mapped[int | None] = mapped_column(Integer, nullable=True)
    red: Mapped[int | None] = mapped_column(Integer, nullable=True)

    # ==================================================
    # Penalties
    # ==================================================

    penalty_won: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalty_committed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalty_scored: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalty_missed: Mapped[int | None] = mapped_column(Integer, nullable=True)
    penalty_saved: Mapped[int | None] = mapped_column(Integer, nullable=True)

    # ==================================================
    # Relationships
    # ==================================================

    player = relationship(
        "Player",
        back_populates="statistics",
    )

    team = relationship(
        "Team",
    )

    league = relationship(
        "League",
    )