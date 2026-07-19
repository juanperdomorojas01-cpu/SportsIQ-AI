from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class Player(BaseModel):
    __tablename__ = "players"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    api_id: Mapped[int] = mapped_column(
        Integer,
        unique=True,
        index=True,
    )

    team_id: Mapped[int] = mapped_column(
        ForeignKey(
            "teams.id",
            ondelete="CASCADE",
        )
    )

    firstname: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    lastname: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    name: Mapped[str] = mapped_column(
        String(150),
    )

    age: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    birth_date: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    birth_place: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    birth_country: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    nationality: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    height: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    weight: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    injured: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    photo: Mapped[str | None] = mapped_column(
        String(300),
        nullable=True,
    )

    # ==========================
    # Relationships
    # ==========================

    team = relationship(
        "Team",
        back_populates="players",
    )

    statistics = relationship(
        "PlayerStatistic",
        back_populates="player",
        cascade="all, delete-orphan",
    )