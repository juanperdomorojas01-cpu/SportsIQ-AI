import httpx

from app.core.config import settings


class APIFootballService:
    BASE_URL = "https://v3.football.api-sports.io"

    def __init__(self):
        self.headers = {
            "x-apisports-key": settings.API_FOOTBALL_KEY
        }

    def _get(self, endpoint: str, params: dict | None = None):
        response = httpx.get(
            f"{self.BASE_URL}{endpoint}",
            headers=self.headers,
            params=params,
            timeout=30,
        )

        response.raise_for_status()

        return response.json()

    # ==========================
    # LEAGUES
    # ==========================

    def get_leagues(self):
        return self._get("/leagues")

    # ==========================
    # TEAMS
    # ==========================

    def get_teams(self, league_id: int, season: int):
        return self._get(
            "/teams",
            {
                "league": league_id,
                "season": season,
            },
        )

    # ==========================
    # PLAYERS
    # ==========================

    def get_players(self, team_id: int, season: int):
        return self._get(
            "/players",
            {
                "team": team_id,
                "season": season,
            },
        )

    def get_player(self, player_id: int, season: int):
        return self._get(
            "/players",
            {
                "id": player_id,
                "season": season,
            },
        )

    # ==========================
    # FIXTURES
    # ==========================

    def get_fixtures(self, league_id: int, season: int):
        return self._get(
            "/fixtures",
            {
                "league": league_id,
                "season": season,
            },
        )

    def get_fixture(self, fixture_id: int):
        return self._get(
            "/fixtures",
            {
                "id": fixture_id,
            },
        )

    def get_fixtures_by_date(self, date: str):
        return self._get(
            "/fixtures",
            {
                "date": date,
            },
        )

    # ==========================
    # STANDINGS
    # ==========================

    def get_standings(self, league_id: int, season: int):
        return self._get(
            "/standings",
            {
                "league": league_id,
                "season": season,
            },
        )

    # ==========================
    # ODDS
    # ==========================

    def get_bookmakers(self):
        return self._get("/odds/bookmakers")

    def get_bets(self):
        return self._get("/odds/bets")

    def get_odds(self, fixture_id: int):
        return self._get(
            "/odds",
            {
                "fixture": fixture_id,
            },
        )

    def get_odds_by_date(self, date: str):
        return self._get(
            "/odds",
            {
                "date": date,
            },
        )