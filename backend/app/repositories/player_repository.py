from sqlalchemy.orm import Session

from app.models.player import Player
from app.repositories.base_repository import BaseRepository


class PlayerRepository(BaseRepository[Player]):
    model = Player

    def __init__(self, db: Session):
        super().__init__(db)

    # ==================================================
    # Queries
    # ==================================================

    def get_by_api_id(self, api_id: int) -> Player | None:
        return (
            self.db.query(Player)
            .filter(Player.api_id == api_id)
            .first()
        )

    def get_by_team(self, team_id: int) -> list[Player]:
        return (
            self.db.query(Player)
            .filter(Player.team_id == team_id)
            .order_by(Player.name.asc())
            .all()
        )

    def get_by_name(self, name: str) -> list[Player]:
        return (
            self.db.query(Player)
            .filter(Player.name.ilike(f"%{name}%"))
            .order_by(Player.name.asc())
            .all()
        )

    def get_injured_players(self) -> list[Player]:
        return (
            self.db.query(Player)
            .filter(Player.injured.is_(True))
            .order_by(Player.name.asc())
            .all()
        )

    # ==================================================
    # Persistence
    # ==================================================

    def create_player(self, data: dict) -> Player:
        player = Player(**data)

        self.db.add(player)
        self.db.commit()
        self.db.refresh(player)

        return player

    def update_player(
        self,
        player: Player,
        data: dict,
    ) -> Player:

        for key, value in data.items():
            setattr(player, key, value)

        self.db.commit()
        self.db.refresh(player)

        return player

    def delete_player(self, player: Player) -> None:
        self.db.delete(player)
        self.db.commit()