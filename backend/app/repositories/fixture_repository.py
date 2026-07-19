from sqlalchemy.orm import Session

from app.models.fixture import Fixture
from app.repositories.base_repository import BaseRepository


class FixtureRepository(BaseRepository[Fixture]):
    model = Fixture

    def __init__(self, db: Session):
        super().__init__(db)

    def get_by_api_id(self, api_id: int) -> Fixture | None:
        return (
            self.db.query(Fixture)
            .filter(Fixture.api_id == api_id)
            .first()
        )