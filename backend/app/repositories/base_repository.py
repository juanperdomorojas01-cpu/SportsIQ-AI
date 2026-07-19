from typing import Generic, Type, TypeVar

from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):

    model: Type[ModelType]

    def __init__(self, db: Session):
        self.db = db

    # ==================================================
    # Queries
    # ==================================================

    def get(self, entity_id: int) -> ModelType | None:
        return (
            self.db.query(self.model)
            .filter(self.model.id == entity_id)
            .first()
        )

    def get_by_api_id(self, api_id: int) -> ModelType | None:
        return (
            self.db.query(self.model)
            .filter(self.model.api_id == api_id)
            .first()
        )

    def get_all(self) -> list[ModelType]:
        return (
            self.db.query(self.model)
            .all()
        )

    def count(self) -> int:
        return (
            self.db.query(self.model)
            .count()
        )

    # ==================================================
    # Persistence
    # ==================================================

    def add(self, entity: ModelType) -> ModelType:
        self.db.add(entity)
        return entity

    def add_and_commit(self, entity: ModelType) -> ModelType:
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()

    def refresh(self, entity: ModelType):
        self.db.refresh(entity)

    def delete(self, entity: ModelType):
        self.db.delete(entity)

    def delete_and_commit(self, entity: ModelType):
        self.db.delete(entity)
        self.db.commit()