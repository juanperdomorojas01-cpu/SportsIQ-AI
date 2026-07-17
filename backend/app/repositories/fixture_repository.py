from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.fixture import Fixture
from app.repositories.base_repository import BaseRepository


class FixtureRepository(BaseRepository[Fixture]):

    def __init__(self, db: Session):
        super().__init__(db, Fixture)

    def get_by_api_id(self, api_id: int) -> Fixture | None:

        stmt = (
            select(Fixture)
            .where(Fixture.api_id == api_id)
        )

        return self.scalar(stmt)