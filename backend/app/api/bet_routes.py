from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.db.database import get_db
from app.models.user import User
from app.schemas.bet import BetCreate
from app.schemas.bet import BetResponse
from app.services.bet_service import BetService

router = APIRouter(
    prefix="/bets",
    tags=["Bets"],
)


@router.post(
    "",
    response_model=BetResponse,
    status_code=201,
)
def create_bet(
    data: BetCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    service = BetService(db)

    try:
        return service.create_bet(
            current_user.id,
            data,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get(
    "/me",
    response_model=list[BetResponse],
)
def get_my_bets(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    service = BetService(db)

    return service.get_my_bets(
        current_user.id,
    )


@router.get(
    "/{bet_id}",
    response_model=BetResponse,
)
def get_bet(
    bet_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    service = BetService(db)

    bet = service.get_bet(bet_id)

    if bet is None:
        raise HTTPException(
            status_code=404,
            detail="Apuesta no encontrada.",
        )

    return bet