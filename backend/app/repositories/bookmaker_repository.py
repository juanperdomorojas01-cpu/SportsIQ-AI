from sqlalchemy.orm import Session

from app.models.bookmaker import Bookmaker
from app.repositories.base_repository import BaseRepository


class BookmakerRepository(BaseRepository[Bookmaker]):
    model = Bookmaker

    def __init__(self, db: Session):
        super().__init__(db)

    def get_by_api_id(self, api_id: int) -> Bookmaker | None:
        return (
            self.db.query(Bookmaker)
            .filter(Bookmaker.api_id == api_id)
            .first()
        )

    def get_by_name(self, name: str) -> Bookmaker | None:
        return (
            self.db.query(Bookmaker)
            .filter(Bookmaker.name == name)
            .first()
        )