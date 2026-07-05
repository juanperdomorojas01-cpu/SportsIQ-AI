from fastapi import FastAPI

from app.api.league_routes import router as league_router
from app.api.team_routes import router as team_router

app = FastAPI(
    title="SportsIQ AI"
)

app.include_router(league_router)
app.include_router(team_router)