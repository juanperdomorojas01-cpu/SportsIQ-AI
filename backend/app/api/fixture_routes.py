from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.fixture_service import FixtureService

router = APIRouter(
    prefix="/fixtures",
    tags=["Fixtures"]
)


@router.post("/sync")
def sync_fixtures(
    league_id: int,
    season: int,
    db: Session = Depends(get_db)
):
    service = FixtureService(db)

    return service.sync_fixtures(
        league_id,
        season
    )