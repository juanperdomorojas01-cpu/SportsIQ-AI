from app.models.odd import Odd
from app.repositories.base_repository import BaseRepository


class OddRepository(BaseRepository[Odd]):

    model = Odd

    def __init__(self, db):

        super().__init__(db)

    def get_by_fixture_bookmaker_bet_type(
        self,
        fixture_id: int,
        bookmaker_id: int,
        bet_type_id: int
    ) -> Odd | None:

        return (
            self.db.query(Odd)
            .filter(
                Odd.fixture_id == fixture_id,
                Odd.bookmaker_id == bookmaker_id,
                Odd.bet_type_id == bet_type_id
            )
            .first()
        )

    def get_by_fixture(
        self,
        fixture_id: int
    ) -> list[Odd]:

        return (
            self.db.query(Odd)
            .filter(
                Odd.fixture_id == fixture_id
            )
            .all()
        )

    def get_by_bookmaker(
        self,
        bookmaker_id: int
    ) -> list[Odd]:

        return (
            self.db.query(Odd)
            .filter(
                Odd.bookmaker_id == bookmaker_id
            )
            .all()
        )

    def get_by_bet_type(
        self,
        bet_type_id: int
    ) -> list[Odd]:

        return (
            self.db.query(Odd)
            .filter(
                Odd.bet_type_id == bet_type_id
            )
            .all()
        )