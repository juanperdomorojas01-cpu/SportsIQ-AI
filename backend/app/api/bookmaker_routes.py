from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.bookmaker_service import BookmakerService

router = APIRouter(
    prefix="/bookmakers",
    tags=["Bookmakers"],
)


@router.post("/sync")
def sync_bookmakers(
    db: Session = Depends(get_db),
):
    service = BookmakerService(db)
    return service.sync_bookmakers()


@router.get("/test")
def test_bookmakers(
    db: Session = Depends(get_db),
):
    service = BookmakerService(db)
    return service.test_bookmakers()