from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel


class BetType(BaseModel):
    __tablename__ = "bet_types"

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
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

    def __repr__(self) -> str:
        return (
            f"<BetType("
            f"id={self.id}, "
            f"name='{self.name}'"
            f")>"
        )