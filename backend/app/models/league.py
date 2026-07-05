from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.team import Team


class League(Base):
    __tablename__ = "leagues"

    id: Mapped[int] = mapped_column(primary_key=True)

    api_id: Mapped[int] = mapped_column(unique=True, index=True)

    name: Mapped[str] = mapped_column(String(100))

    country: Mapped[str] = mapped_column(String(100))

    season: Mapped[int]

    logo: Mapped[str] = mapped_column(String(500))

    teams: Mapped[list["Team"]] = relationship(
        back_populates="league",
        cascade="all, delete-orphan"
    )