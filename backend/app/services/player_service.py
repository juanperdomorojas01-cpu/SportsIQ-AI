from sqlalchemy.orm import Session

from app.models.player import Player
from app.models.player_statistic import PlayerStatistic
from app.repositories.league_repository import LeagueRepository
from app.repositories.player_repository import PlayerRepository
from app.repositories.player_statistic_repository import (
    PlayerStatisticRepository,
)
from app.repositories.team_repository import TeamRepository
from app.services.api_football import APIFootballService


class PlayerService:

    def __init__(self, db: Session):
        self.db = db

        self.api = APIFootballService()

        self.player_repository = PlayerRepository(db)
        self.player_statistic_repository = PlayerStatisticRepository(db)
        self.team_repository = TeamRepository(db)
        self.league_repository = LeagueRepository(db)

    # ==========================================================
    # PUBLIC
    # ==========================================================

    def sync_players(
        self,
        team_api_id: int,
        season: int,
    ):
        data = self.api.get_players(team_api_id, season)

        synced_players = 0
        synced_statistics = 0

        for item in data["response"]:

            player = self.save_player(
                item["player"],
                team_api_id,
            )

            synced_players += 1

            for statistic in item["statistics"]:

                self.save_statistic(
                    player,
                    statistic,
                )

                synced_statistics += 1

        return {
            "players": synced_players,
            "statistics": synced_statistics,
        }

    # ==========================================================
    # PLAYER
    # ==========================================================

    def save_player(
        self,
        player_data: dict,
        team_api_id: int,
    ) -> Player:

        team = self.team_repository.get_by_api_id(team_api_id)

        if team is None:
            raise ValueError(
                f"Team api_id={team_api_id} no existe."
            )

        player = self.player_repository.get_by_api_id(
            player_data["id"]
        )

        values = self.map_player(
            player_data,
            team.id,
        )

        if player:

            player = self.player_repository.update_player(
                player,
                values,
            )

        else:

            player = self.player_repository.create_player(
                values,
            )

        return player

    # ==========================================================
    # STATISTICS
    # ==========================================================

    def save_statistic(
        self,
        player: Player,
        statistic: dict,
    ) -> PlayerStatistic:

        team = self.team_repository.get_by_api_id(
            statistic["team"]["id"]
        )

        league = self.league_repository.get_by_api_id(
            statistic["league"]["id"]
        )

        if team is None or league is None:
            return

        values = self.map_statistic(
            player.id,
            team.id,
            league.id,
            statistic,
        )

        player_statistic = (
            self.player_statistic_repository.get_by_unique(
                player.id,
                team.id,
                league.id,
                statistic["league"]["season"],
            )
        )

        if player_statistic:

            player_statistic = (
                self.player_statistic_repository.update_statistic(
                    player_statistic,
                    values,
                )
            )

        else:

            player_statistic = (
                self.player_statistic_repository.create_statistic(
                    values,
                )
            )

        return player_statistic

    # ==========================================================
    # MAPPERS
    # ==========================================================

    def map_player(
        self,
        player: dict,
        team_id: int,
    ):

        birth = player.get("birth") or {}

        return {
            "api_id": player["id"],
            "team_id": team_id,
            "firstname": player.get("firstname"),
            "lastname": player.get("lastname"),
            "name": player.get("name"),
            "age": player.get("age"),
            "birth_date": birth.get("date"),
            "birth_place": birth.get("place"),
            "birth_country": birth.get("country"),
            "nationality": player.get("nationality"),
            "height": player.get("height"),
            "weight": player.get("weight"),
            "injured": player.get("injured"),
            "photo": player.get("photo"),
        }

    def map_statistic(
        self,
        player_id: int,
        team_id: int,
        league_id: int,
        statistic: dict,
    ):

        games = statistic.get("games", {})
        substitutes = statistic.get("substitutes", {})
        shots = statistic.get("shots", {})
        goals = statistic.get("goals", {})
        passes = statistic.get("passes", {})
        tackles = statistic.get("tackles", {})
        duels = statistic.get("duels", {})
        dribbles = statistic.get("dribbles", {})
        fouls = statistic.get("fouls", {})
        cards = statistic.get("cards", {})
        penalty = statistic.get("penalty", {})

        rating = games.get("rating")

        return {

            "player_id": player_id,
            "team_id": team_id,
            "league_id": league_id,
            "season": statistic["league"]["season"],

            "appearances": games.get("appearences"),
            "lineups": games.get("lineups"),
            "minutes": games.get("minutes"),
            "number": games.get("number"),
            "position": games.get("position"),
            "rating": float(rating) if rating else None,
            "captain": games.get("captain"),

            "sub_in": substitutes.get("in"),
            "sub_out": substitutes.get("out"),
            "bench": substitutes.get("bench"),

            "shots_total": shots.get("total"),
            "shots_on": shots.get("on"),

            "goals": goals.get("total"),
            "assists": goals.get("assists"),
            "goals_conceded": goals.get("conceded"),
            "saves": goals.get("saves"),

            "passes_total": passes.get("total"),
            "passes_key": passes.get("key"),
            "passes_accuracy": passes.get("accuracy"),

            "tackles_total": tackles.get("total"),
            "blocks": tackles.get("blocks"),
            "interceptions": tackles.get("interceptions"),

            "duels_total": duels.get("total"),
            "duels_won": duels.get("won"),

            "dribbles_attempts": dribbles.get("attempts"),
            "dribbles_success": dribbles.get("success"),
            "dribbled_past": dribbles.get("past"),

            "fouls_drawn": fouls.get("drawn"),
            "fouls_committed": fouls.get("committed"),

            "yellow": cards.get("yellow"),
            "yellow_red": cards.get("yellowred"),
            "red": cards.get("red"),

            "penalty_won": penalty.get("won"),
            "penalty_committed": penalty.get("commited"),
            "penalty_scored": penalty.get("scored"),
            "penalty_missed": penalty.get("missed"),
            "penalty_saved": penalty.get("saved"),
        }