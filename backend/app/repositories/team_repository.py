from sqlalchemy import select
from sqlalchemy.orm import Session

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