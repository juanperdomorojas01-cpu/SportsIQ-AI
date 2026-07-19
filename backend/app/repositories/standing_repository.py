from sqlalchemy.orm import Session

from app.models.standing import Standing
from app.repositories.base_repository import BaseRepository


class StandingRepository(BaseRepository[Standing]):
    model = Standing

    def __init__(self, db: Session):
        super().__init__(db)

    def get_by_team_and_season(
        self,
        team_id: int,
        season: int,
    ) -> Standing | None:
        return (
            self.db.query(Standing)
            .filter(
                Standing.team_id == team_id,
                Standing.season == season,
            )
            .first()
        )