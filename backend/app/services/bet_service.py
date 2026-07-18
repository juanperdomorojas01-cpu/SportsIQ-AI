from decimal import Decimal

from sqlalchemy.orm import Session

from app.models.bet import Bet
from app.models.enums import BetStatus
from app.models.enums import TransactionType
from app.models.transaction import Transaction
from app.repositories.bankroll_repository import BankrollRepository
from app.repositories.bet_market_repository import BetMarketRepository
from app.repositories.bet_repository import BetRepository
from app.repositories.bet_type_repository import BetTypeRepository
from app.repositories.bookmaker_repository import BookmakerRepository
from app.repositories.fixture_repository import FixtureRepository
from app.repositories.transaction_repository import TransactionRepository
from app.schemas.bet import BetCreate


class BetService:

    def __init__(self, db: Session):
        self.db = db

        self.bankroll_repository = BankrollRepository(db)
        self.bet_repository = BetRepository(db)
        self.transaction_repository = TransactionRepository(db)

        self.fixture_repository = FixtureRepository(db)
        self.bookmaker_repository = BookmakerRepository(db)
        self.market_repository = BetMarketRepository(db)
        self.bet_type_repository = BetTypeRepository(db)

    def create_bet(
        self,
        user_id: int,
        data: BetCreate,
    ) -> Bet:

        bankroll = self.bankroll_repository.get_by_user_id(user_id)

        if bankroll is None:
            raise ValueError(
                "El usuario no tiene un bankroll registrado."
            )

        if bankroll.current_balance < data.stake:
            raise ValueError(
                "Saldo insuficiente para registrar la apuesta."
            )

        fixture = self.fixture_repository.get_by_id(data.fixture_id)

        if fixture is None:
            raise ValueError(
                "El fixture no existe."
            )

        bookmaker = self.bookmaker_repository.get_by_id(
            data.bookmaker_id
        )

        if bookmaker is None:
            raise ValueError(
                "La casa de apuestas no existe."
            )

        market = self.market_repository.get_by_id(
            data.market_id
        )

        if market is None:
            raise ValueError(
                "El mercado no existe."
            )

        bet_type = self.bet_type_repository.get_by_id(
            data.bet_type_id
        )

        if bet_type is None:
            raise ValueError(
                "El tipo de apuesta no existe."
            )

        try:

            balance_before = Decimal(bankroll.current_balance)
            balance_after = balance_before - Decimal(data.stake)

            potential_return = (
                Decimal(data.stake)
                * Decimal(data.odds)
            ).quantize(
                Decimal("0.01")
            )

            bet = Bet(
                bankroll_id=bankroll.id,
                fixture_id=data.fixture_id,
                bookmaker_id=data.bookmaker_id,
                market_id=data.market_id,
                bet_type_id=data.bet_type_id,
                selection=data.selection,
                stake=data.stake,
                odds=data.odds,
                potential_return=potential_return,
                payout=None,
                profit=None,
                status=BetStatus.PENDING,
                notes=data.notes,
            )

            self.bet_repository.add(bet)
            self.bet_repository.flush()

            transaction = Transaction(
                bankroll_id=bankroll.id,
                bet_id=bet.id,
                type=TransactionType.BET_PLACED,
                amount=data.stake,
                balance_before=balance_before,
                balance_after=balance_after,
                description=f"Apuesta #{bet.id}",
            )

            self.transaction_repository.add(transaction)

            bankroll.current_balance = balance_after

            self.db.commit()

            self.bet_repository.refresh(bet)

            return bet

        except Exception:
            self.db.rollback()
            raise

    def get_my_bets(
        self,
        user_id: int,
    ) -> list[Bet]:

        bankroll = self.bankroll_repository.get_by_user_id(user_id)

        if bankroll is None:
            return []

        return self.bet_repository.get_by_bankroll(
            bankroll.id
        )

    def get_bet(
        self,
        bet_id: int,
    ) -> Bet | None:

        return self.bet_repository.get_by_id(
            bet_id
        )