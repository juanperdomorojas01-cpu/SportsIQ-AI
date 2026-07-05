from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.team_service import TeamService


router = APIRouter(
    prefix="/teams",
    tags=["Teams"]
)


@router.post("/sync")
def sync_teams(
    league_id: int,
    season: int,
    db: Session = Depends(get_db)
):
    service = TeamService(db)

    return service.sync_teams(league_id, season)