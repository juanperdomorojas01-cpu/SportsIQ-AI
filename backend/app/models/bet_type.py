from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel


class BetType(BaseModel):
    __tablename__ = "bet_types"

    api_id: Mapped[int] = mapped_column(
        unique=True,
        index=True,
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        default=True,
        nullable=False,
    )

    bets = relationship(
        "Bet",
        back_populates="bet_type",
    )

    odds = relationship(
        "Odd",
        back_populates="bet_type",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return (
            f"<BetType("
            f"id={self.id}, "
            f"api_id={self.api_id}, "
            f"name='{self.name}'"
            f")>"
        )