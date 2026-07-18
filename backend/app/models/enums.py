from enum import Enum


class AccountStatus(str, Enum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"
    EXPIRED = "EXPIRED"


class BetStatus(str, Enum):
    PENDING = "PENDING"
    SETTLED = "SETTLED"
    VOID = "VOID"
    CASH_OUT = "CASH_OUT"


class BetResult(str, Enum):
    WON = "WON"
    LOST = "LOST"
    HALF_WON = "HALF_WON"
    HALF_LOST = "HALF_LOST"
    PUSH = "PUSH"


class TransactionType(str, Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL"
    BET_PLACED = "BET_PLACED"
    BET_SETTLED = "BET_SETTLED"
    BONUS = "BONUS"
    REFUND = "REFUND"
    ADJUSTMENT = "ADJUSTMENT"