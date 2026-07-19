from fastapi import APIRouter

from app.services.api_football import APIFootballService

router = APIRouter(
    prefix="/odds",
    tags=["Odds"],
)


@router.get("/test/{fixture_id}")
def test_odds(fixture_id: int):

    api = APIFootballService()

    return api.get_odds(fixture_id)


@router.get("/fixtures/{date}")
def fixtures_by_date(date: str):

    api = APIFootballService()

    return api.get_fixtures_by_date(date)