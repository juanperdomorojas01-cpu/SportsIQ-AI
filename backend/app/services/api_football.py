import httpx

from app.core.config import settings


class APIFootballService:

    BASE_URL = "https://v3.football.api-sports.io"

    def __init__(self):

        self.headers = {
            "x-apisports-key": settings.API_FOOTBALL_KEY
        }

    def get_leagues(self):

        response = httpx.get(
            f"{self.BASE_URL}/leagues",
            headers=self.headers,
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    def get_teams(
        self,
        league_id: int,
        season: int
    ):

        response = httpx.get(
            f"{self.BASE_URL}/teams",
            headers=self.headers,
            params={
                "league": league_id,
                "season": season
            },
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    def get_fixtures(
        self,
        league_id: int,
        season: int
    ):

        response = httpx.get(
            f"{self.BASE_URL}/fixtures",
            headers=self.headers,
            params={
                "league": league_id,
                "season": season
            },
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    def get_standings(
        self,
        league_id: int,
        season: int
    ):

        response = httpx.get(
            f"{self.BASE_URL}/standings",
            headers=self.headers,
            params={
                "league": league_id,
                "season": season
            },
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    # ==========================================================
    # BOOKMAKERS
    # ==========================================================

    def get_bookmakers(self):

        response = httpx.get(
            f"{self.BASE_URL}/odds/bookmakers",
            headers=self.headers,
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    # ==========================================================
    # BET TYPES
    # ==========================================================

    def get_bets(self):

        response = httpx.get(
            f"{self.BASE_URL}/odds/bets",
            headers=self.headers,
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    # ==========================================================
    # ODDS
    # ==========================================================

    def get_odds(
        self,
        fixture_id: int
    ):

        response = httpx.get(
            f"{self.BASE_URL}/odds",
            headers=self.headers,
            params={
                "fixture": fixture_id
            },
            timeout=30
        )

        response.raise_for_status()

        return response.json()