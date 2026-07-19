from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.repositories.player_repository import PlayerRepository
from app.services.player_service import PlayerService

router = APIRouter(
    prefix="/players",
    tags=["Players"],
)


@router.post("/sync")
def sync_players(
    team_api_id: int,
    season: int,
    db: Session = Depends(get_db),
):
    """
    Sincroniza todos los jugadores de un equipo para una temporada.
    """

    service = PlayerService(db)

    try:
        return service.sync_players(
            team_api_id,
            season,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get("/")
def get_players(
    db: Session = Depends(get_db),
):
    repository = PlayerRepository(db)

    return repository.get_all()


@router.get("/team/{team_id}")
def get_players_by_team(
    team_id: int,
    db: Session = Depends(get_db),
):
    repository = PlayerRepository(db)

    return repository.get_by_team(team_id)


@router.get("/{player_id}")
def get_player(
    player_id: int,
    db: Session = Depends(get_db),
):
    repository = PlayerRepository(db)

    player = repository.get(player_id)

    if player is None:
        raise HTTPException(
            status_code=404,
            detail="Player not found",
        )

    return player