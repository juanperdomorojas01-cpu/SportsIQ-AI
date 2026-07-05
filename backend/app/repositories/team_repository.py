from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.team import Team
from app.repositories.base_repository import BaseRepository


class TeamRepository(BaseRepository[Team]):

    def __init__(self, db: Session):
        super().__init__(db, Team)

    def get_by_api_id(self, api_id: int) -> Team | None:

        stmt = (
            select(Team)
            .where(Team.api_id == api_id)
        )

        return self.scalar(stmt)

    def upsert(self, team: Team) -> Team:

        existing = self.get_by_api_id(team.api_id)

        if existing:

            existing.name = team.name
            existing.code = team.code
            existing.country = team.country
            existing.founded = team.founded
            existing.national = team.national
            existing.logo = team.logo
            existing.league_id = team.league_id

            return existing

        self.add(team)

        return team