from decimal import Decimal

from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel


class OddValue(BaseModel):
    __tablename__ = "odd_values"

    odd_id: Mapped[int] = mapped_column(
        ForeignKey("odds.id"),
        nullable=False,
        index=True,
    )

    value: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    price: Mapped[Decimal] = mapped_column(
        Numeric(8, 2),
        nullable=False,
    )

    odd = relationship(
        "Odd",
        back_populates="values",
    )

    def __repr__(self) -> str:
        return (
            f"<OddValue("
            f"id={self.id}, "
            f"value='{self.value}', "
            f"price={self.price}"
            f")>"
        )