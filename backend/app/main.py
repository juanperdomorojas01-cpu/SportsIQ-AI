from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.dashboard_routes import router as dashboard_router
from app.api.fixture_routes import router as fixture_router
from app.api.league_routes import router as league_router
from app.api.standing_routes import router as standing_router
from app.api.team_routes import router as team_router

app = FastAPI(
    title="SportsIQ AI",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dashboard_router)
app.include_router(league_router)
app.include_router(team_router)
app.include_router(fixture_router)
app.include_router(standing_router)