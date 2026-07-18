from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.db.database import get_db
from app.models.user import User
from app.repositories.bankroll_repository import BankrollRepository
from app.schemas.bankroll import BankrollCreate
from app.schemas.bankroll import BankrollResponse
from app.services.bankroll_service import BankrollService

router = APIRouter(
    prefix="/bankroll",
    tags=["Bankroll"],
)


def get_bankroll_service(
    db: Session = Depends(get_db),
) -> BankrollService:

    repository = BankrollRepository(db)

    return BankrollService(repository)


@router.post(
    "",
    response_model=BankrollResponse,
)
def create_bankroll(
    bankroll: BankrollCreate,
    current_user: User = Depends(get_current_user),
    service: BankrollService = Depends(get_bankroll_service),
):

    try:
        return service.create_bankroll(
            current_user.id,
            bankroll,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get(
    "/me",
    response_model=BankrollResponse,
)
def get_my_bankroll(
    current_user: User = Depends(get_current_user),
    service: BankrollService = Depends(get_bankroll_service),
):

    bankroll = service.get_my_bankroll(current_user.id)

    if bankroll is None:
        raise HTTPException(
            status_code=404,
            detail="El usuario no tiene bankroll.",
        )

    return bankroll