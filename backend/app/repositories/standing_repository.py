from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.standing import Standing
from app.repositories.base_repository import BaseRepository


class StandingRepository(BaseRepository[Standing]):

    def __init__(self, db: Session):
        super().__init__(db, Standing)

    def get_by_team_and_season(
        self,
        team_id: int,
        season: int
    ) -> Standing | None:

        stmt = (
            select(Standing)
            .where(
                Standing.team_id == team_id,
                Standing.season == season
            )
        )

        return self.scalar(stmt)