from sqlalchemy.orm import Session

from app.repositories.fixture_repository import FixtureRepository
from app.repositories.league_repository import LeagueRepository
from app.repositories.standing_repository import StandingRepository
from app.repositories.team_repository import TeamRepository
from app.schemas.dashboard import DashboardResponse


class DashboardService:

    def __init__(self, db: Session):
        self.league_repository = LeagueRepository(db)
        self.team_repository = TeamRepository(db)
        self.fixture_repository = FixtureRepository(db)
        self.standing_repository = StandingRepository(db)

    def get_dashboard(self) -> DashboardResponse:

        return DashboardResponse(
            leagues=self.league_repository.count(),
            teams=self.team_repository.count(),
            fixtures=self.fixture_repository.count(),
            standings=self.standing_repository.count(),
            last_sync=None,
        )