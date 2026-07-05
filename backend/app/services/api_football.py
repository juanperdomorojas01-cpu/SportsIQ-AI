import httpx

from app.config import settings


class APIFootballService:
    BASE_URL = "https://v3.football.api-sports.io"

    def __init__(self):
        self.headers = {
            "x-apisports-key": settings.API_FOOTBALL_KEY
        }

    def get_leagues(self):
        url = f"{self.BASE_URL}/leagues"

        response = httpx.get(
            url,
            headers=self.headers,
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    def get_teams(self, league_id: int, season: int):
        url = f"{self.BASE_URL}/teams"

        response = httpx.get(
            url,
            headers=self.headers,
            params={
                "league": league_id,
                "season": season
            },
            timeout=30
        )

        response.raise_for_status()

        return response.json()