from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class BankrollCreate(BaseModel):
    initial_balance: Decimal
    currency: str = "USD"


class BankrollResponse(BaseModel):
    id: int
    user_id: int
    initial_balance: Decimal
    current_balance: Decimal
    currency: str
    total_profit: Decimal
    total_loss: Decimal

    model_config = ConfigDict(from_attributes=True)