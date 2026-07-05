from sqlalchemy.orm import Session

from app.models.league import League
from app.repositories.league_repository import LeagueRepository
from app.services.api_football import APIFootballService


class LeagueService:

    def __init__(self, db: Session):
        self.db = db
        self.repository = LeagueRepository(db)
        self.api = APIFootballService()

    def sync_leagues(self):

        data = self.api.get_leagues()

        created = 0

        try:

            for item in data["response"]:

                league_data = item["league"]
                country_data = item["country"]

                exists = self.repository.get_by_api_id(
                    league_data["id"]
                )

                if exists:
                    continue

                league = League(
                    api_id=league_data["id"],
                    name=league_data["name"],
                    country=country_data["name"],
                    season=0,
                    logo=league_data["logo"]
                )

                self.repository.add(league)

                created += 1

            self.repository.commit()

            return {
                "created": created
            }

        except Exception:
            self.repository.rollback()
            raise