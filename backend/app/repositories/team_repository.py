from sqlalchemy.orm import Session

from app.models.team import Team
from app.repositories.base_repository import BaseRepository


class TeamRepository(BaseRepository[Team]):
    model = Team

    def __init__(self, db: Session):
        super().__init__(db)

    def get_by_api_id(self, api_id: int) -> Team | None:
        return (
            self.db.query(Team)
            .filter(Team.api_id == api_id)
            .first()
        )