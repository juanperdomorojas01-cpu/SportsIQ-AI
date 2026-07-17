from datetime import datetime

from pydantic import BaseModel


class DashboardResponse(BaseModel):
    leagues: int
    teams: int
    fixtures: int
    standings: int
    last_sync: datetime | None