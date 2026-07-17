from datetime import datetime

from sqlalchemy.orm import Session

from app.models.fixture import Fixture
from app.repositories.fixture_repository import FixtureRepository
from app.repositories.league_repository import LeagueRepository
from app.repositories.team_repository import TeamRepository
from app.services.api_football import APIFootballService


class FixtureService:

    def __init__(self, db: Session):

        self.repository = FixtureRepository(db)
        self.league_repository = LeagueRepository(db)
        self.team_repository = TeamRepository(db)
        self.api = APIFootballService()

    def sync_fixtures(self, league_id: int, season: int):

        data = self.api.get_fixtures(
            league_id,
            season
        )

        league = self.league_repository.get_by_api_id(
            league_id
        )

        if league is None:
            raise ValueError(
                f"No existe una liga con api_id={league_id}"
            )

        created = 0

        try:

            for item in data["response"]:

                fixture_data = item["fixture"]
                teams_data = item["teams"]
                goals_data = item["goals"]

                exists = self.repository.get_by_api_id(
                    fixture_data["id"]
                )

                if exists:
                    continue

                home_team = self.team_repository.get_by_api_id(
                    teams_data["home"]["id"]
                )

                away_team = self.team_repository.get_by_api_id(
                    teams_data["away"]["id"]
                )

                if home_team is None or away_team is None:
                    continue

                fixture = Fixture(
                    api_id=fixture_data["id"],
                    referee=fixture_data["referee"],
                    timezone=fixture_data["timezone"],
                    date=datetime.fromisoformat(
                        fixture_data["date"].replace("Z", "+00:00")
                    ),
                    timestamp=fixture_data["timestamp"],
                    status=fixture_data["status"]["short"],
                    league_id=league.id,
                    home_team_id=home_team.id,
                    away_team_id=away_team.id,
                    home_goals=goals_data["home"],
                    away_goals=goals_data["away"]
                )

                self.repository.add(fixture)

                created += 1

            self.repository.commit()

            return {
                "created": created
            }

        except Exception:

            self.repository.rollback()

            raise