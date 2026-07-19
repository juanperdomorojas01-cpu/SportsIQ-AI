from sqlalchemy.orm import Session

from app.models.player_statistic import PlayerStatistic
from app.repositories.base_repository import BaseRepository


class PlayerStatisticRepository(BaseRepository[PlayerStatistic]):
    model = PlayerStatistic

    def __init__(self, db: Session):
        super().__init__(db)

    # ==================================================
    # Queries
    # ==================================================

    def get_by_unique(
        self,
        player_id: int,
        team_id: int,
        league_id: int,
        season: int,
    ) -> PlayerStatistic | None:
        return (
            self.db.query(PlayerStatistic)
            .filter(
                PlayerStatistic.player_id == player_id,
                PlayerStatistic.team_id == team_id,
                PlayerStatistic.league_id == league_id,
                PlayerStatistic.season == season,
            )
            .first()
        )

    def get_by_player(
        self,
        player_id: int,
    ) -> list[PlayerStatistic]:
        return (
            self.db.query(PlayerStatistic)
            .filter(PlayerStatistic.player_id == player_id)
            .all()
        )

    def get_by_team(
        self,
        team_id: int,
    ) -> list[PlayerStatistic]:
        return (
            self.db.query(PlayerStatistic)
            .filter(PlayerStatistic.team_id == team_id)
            .all()
        )

    def get_by_league(
        self,
        league_id: int,
    ) -> list[PlayerStatistic]:
        return (
            self.db.query(PlayerStatistic)
            .filter(PlayerStatistic.league_id == league_id)
            .all()
        )

    def get_by_season(
        self,
        season: int,
    ) -> list[PlayerStatistic]:
        return (
            self.db.query(PlayerStatistic)
            .filter(PlayerStatistic.season == season)
            .all()
        )

    # ==================================================
    # Persistence
    # ==================================================

    def create_statistic(
        self,
        data: dict,
    ) -> PlayerStatistic:

        statistic = PlayerStatistic(**data)

        self.db.add(statistic)
        self.db.commit()
        self.db.refresh(statistic)

        return statistic

    def update_statistic(
        self,
        statistic: PlayerStatistic,
        data: dict,
    ) -> PlayerStatistic:

        for key, value in data.items():
            setattr(statistic, key, value)

        self.db.commit()
        self.db.refresh(statistic)

        return statistic

    def delete_statistic(
        self,
        statistic: PlayerStatistic,
    ) -> None:

        self.db.delete(statistic)
        self.db.commit()