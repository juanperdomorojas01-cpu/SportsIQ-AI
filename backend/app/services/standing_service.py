from sqlalchemy.orm import Session

from app.models.standing import Standing
from app.repositories.league_repository import LeagueRepository
from app.repositories.standing_repository import StandingRepository
from app.repositories.team_repository import TeamRepository
from app.services.api_football import APIFootballService


class StandingService:

    def __init__(self, db: Session):

        self.repository = StandingRepository(db)
        self.team_repository = TeamRepository(db)
        self.league_repository = LeagueRepository(db)

        self.api = APIFootballService()

    def sync_standings(
        self,
        league_id: int,
        season: int
    ):

        data = self.api.get_standings(
            league_id,
            season
        )

        league = self.league_repository.get_by_api_id(
            league_id
        )

        if league is None:
            raise ValueError("League not found")

        created = 0

        try:

            standings = data["response"][0]["league"]["standings"][0]

            for item in standings:

                team = self.team_repository.get_by_api_id(
                    item["team"]["id"]
                )

                if team is None:
                    continue

                exists = self.repository.get_by_team_and_season(
                    team.id,
                    season
                )

                if exists:
                    continue

                standing = Standing(

                    league_id=league.id,

                    team_id=team.id,

                    season=season,

                    position=item["rank"],

                    points=item["points"],

                    played=item["all"]["played"],

                    win=item["all"]["win"],

                    draw=item["all"]["draw"],

                    lose=item["all"]["lose"],

                    goals_for=item["all"]["goals"]["for"],

                    goals_against=item["all"]["goals"]["against"],

                    goal_difference=item["goalsDiff"],

                    form=item["form"]

                )

                self.repository.add(standing)

                created += 1

            self.repository.commit()

            return {
                "created": created
            }

        except Exception:

            self.repository.rollback()

            raise