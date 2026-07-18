from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict

from app.models.enums import TransactionType


class TransactionResponse(BaseModel):
    id: int
    bankroll_id: int
    bet_id: int | None
    type: TransactionType
    amount: Decimal
    balance_before: Decimal
    balance_after: Decimal
    description: str | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)