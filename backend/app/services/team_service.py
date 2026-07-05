from sqlalchemy.orm import Session

from app.models.team import Team
from app.repositories.team_repository import TeamRepository
from app.repositories.league_repository import LeagueRepository
from app.services.api_football import APIFootballService


class TeamService:

    def __init__(self, db: Session):
        self.repository = TeamRepository(db)
        self.league_repository = LeagueRepository(db)
        self.api = APIFootballService()

    def sync_teams(self, league_id: int, season: int):

        data = self.api.get_teams(league_id, season)

        league = self.league_repository.get_by_api_id(league_id)

        if league is None:
            raise ValueError(
                f"No existe una liga con api_id={league_id}. "
                "Primero sincroniza las ligas."
            )

        processed = 0

        try:

            for item in data["response"]:

                team_data = item["team"]

                team = Team(
                    api_id=team_data["id"],
                    name=team_data["name"],
                    code=team_data.get("code"),
                    country=team_data["country"],
                    founded=team_data.get("founded"),
                    national=team_data["national"],
                    logo=team_data["logo"],
                    league_id=league.id,
                )

                self.repository.upsert(team)

                processed += 1

            self.repository.commit()

            return {
                "processed": processed
            }

        except Exception:
            self.repository.rollback()
            raise