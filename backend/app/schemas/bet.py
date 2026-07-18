from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict

from app.models.enums import BetResult
from app.models.enums import BetStatus


class BetCreate(BaseModel):
    fixture_id: int
    bookmaker_id: int
    market_id: int
    bet_type_id: int
    selection: str
    odds: Decimal
    stake: Decimal
    notes: str | None = None


class BetResponse(BaseModel):
    id: int

    bankroll_id: int
    fixture_id: int
    bookmaker_id: int
    market_id: int
    bet_type_id: int

    selection: str

    stake: Decimal
    odds: Decimal

    potential_return: Decimal
    payout: Decimal | None
    profit: Decimal | None

    status: BetStatus
    result: BetResult | None

    placed_at: datetime
    settled_at: datetime | None

    notes: str | None

    model_config = ConfigDict(from_attributes=True)