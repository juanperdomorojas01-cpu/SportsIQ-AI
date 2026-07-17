from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.standing_service import StandingService

router = APIRouter(
    prefix="/standings",
    tags=["Standings"]
)


@router.post("/sync")
def sync_standings(
    league_id: int,
    season: int,
    db: Session = Depends(get_db)
):

    service = StandingService(db)

    return service.sync_standings(
        league_id,
        season
    )