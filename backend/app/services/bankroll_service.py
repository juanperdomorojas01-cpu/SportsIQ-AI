from app.models.bankroll import Bankroll
from app.repositories.bankroll_repository import BankrollRepository
from app.schemas.bankroll import BankrollCreate


class BankrollService:

    def __init__(
        self,
        bankroll_repository: BankrollRepository,
    ):
        self.bankroll_repository = bankroll_repository

    def create_bankroll(
        self,
        user_id: int,
        data: BankrollCreate,
    ) -> Bankroll:

        existing = self.bankroll_repository.get_by_user_id(user_id)

        if existing:
            raise ValueError(
                "El usuario ya tiene un bankroll."
            )

        bankroll = Bankroll(
            user_id=user_id,
            initial_balance=data.initial_balance,
            current_balance=data.initial_balance,
            currency=data.currency,
            total_profit=0,
            total_loss=0,
        )

        return self.bankroll_repository.add(bankroll)

    def get_my_bankroll(
        self,
        user_id: int,
    ) -> Bankroll | None:

        return self.bankroll_repository.get_by_user_id(user_id)