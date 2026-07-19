from app.models.odd_value import OddValue
from app.repositories.base_repository import BaseRepository


class OddValueRepository(BaseRepository[OddValue]):

    model = OddValue

    def __init__(self, db):

        super().__init__(db)

    def get_by_odd(
        self,
        odd_id: int
    ) -> list[OddValue]:

        return (
            self.db.query(OddValue)
            .filter(
                OddValue.odd_id == odd_id
            )
            .all()
        )

    def get_by_odd_and_value(
        self,
        odd_id: int,
        value: str
    ) -> OddValue | None:

        return (
            self.db.query(OddValue)
            .filter(
                OddValue.odd_id == odd_id,
                OddValue.value == value
            )
            .first()
        )