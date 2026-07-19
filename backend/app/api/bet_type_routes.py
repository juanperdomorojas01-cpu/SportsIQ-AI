from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.bet_type_service import BetTypeService

router = APIRouter(
    prefix="/bet-types",
    tags=["Bet Types"],
)


@router.get("/test")
def test_bet_types(
    db: Session = Depends(get_db),
):
    service = BetTypeService(db)
    return service.test_bet_types()


@router.post("/sync")
def sync_bet_types(
    db: Session = Depends(get_db),
):
    service = BetTypeService(db)
    return service.sync_bet_types()