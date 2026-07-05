from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.league_service import LeagueService

router = APIRouter(
    prefix="/leagues",
    tags=["Leagues"]
)


@router.post("/sync")
def sync_leagues(db: Session = Depends(get_db)):
    service = LeagueService(db)
    return service.sync_leagues()