from typing import Generic, TypeVar

from sqlalchemy import func, select
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):

    def __init__(
        self,
        db: Session,
        model: type[ModelType],
    ):
        self.db = db
        self.model = model

    def get_by_id(
        self,
        entity_id: int,
    ) -> ModelType | None:

        stmt = (
            select(self.model)
            .where(self.model.id == entity_id)
        )

        return self.db.scalar(stmt)

    def get_all(self) -> list[ModelType]:

        stmt = select(self.model)

        return list(self.db.scalars(stmt))

    def add(
        self,
        entity: ModelType,
    ) -> ModelType:

        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)

        return entity

    def commit(self):

        self.db.commit()

    def rollback(self):

        self.db.rollback()

    def refresh(
        self,
        entity: ModelType,
    ):

        self.db.refresh(entity)

    def flush(self):

        self.db.flush()

    def scalar(self, stmt):

        return self.db.scalar(stmt)

    def scalars(self, stmt):

        return self.db.scalars(stmt)

    def count(self) -> int:

        stmt = select(func.count()).select_from(self.model)

        return self.db.scalar(stmt) or 0