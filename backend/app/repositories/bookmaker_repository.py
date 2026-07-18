from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.bookmaker import Bookmaker
from app.repositories.base_repository import BaseRepository


class BookmakerRepository(BaseRepository[Bookmaker]):

    def __init__(self, db: Session):
        super().__init__(db, Bookmaker)

    def get_by_api_id(
        self,
        api_id: int,
    ) -> Bookmaker | None:

        stmt = (
            select(Bookmaker)
            .where(Bookmaker.api_id == api_id)
        )

        return self.scalar(stmt)

    def get_by_name(
        self,
        name: str,
    ) -> Bookmaker | None:

        stmt = (
            select(Bookmaker)
            .where(Bookmaker.name == name)
        )

        return self.scalar(stmt)