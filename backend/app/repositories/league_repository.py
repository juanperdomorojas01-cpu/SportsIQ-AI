from sqlalchemy.orm import Session

from app.models.league import League
from app.repositories.base_repository import BaseRepository


class LeagueRepository(BaseRepository[League]):
    model = League

    def __init__(self, db: Session):
        super().__init__(db)

    def get_by_api_id(self, api_id: int) -> League | None:
        return (
            self.db.query(League)
            .filter(League.api_id == api_id)
            .first()
        )