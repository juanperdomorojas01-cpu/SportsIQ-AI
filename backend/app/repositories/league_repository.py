from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.league import League
from app.repositories.base_repository import BaseRepository


class LeagueRepository(BaseRepository[League]):

    def __init__(self, db: Session):
        super().__init__(db, League)

    def get_by_api_id(self, api_id: int) -> League | None:

        stmt = (
            select(League)
            .where(League.api_id == api_id)
        )

        return self.scalar(stmt)