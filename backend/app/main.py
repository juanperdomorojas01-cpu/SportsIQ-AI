from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth_routes import router as auth_router
from app.api.dashboard_routes import router as dashboard_router
from app.api.fixture_routes import router as fixture_router
from app.api.league_routes import router as league_router
from app.api.standing_routes import router as standing_router
from app.api.team_routes import router as team_router
from app.api.bookmaker_routes import router as bookmaker_router
from app.api.bankroll_routes import router as bankroll_router
from app.api.bet_routes import router as bet_router

from app.db.database import SessionLocal
from app.db.seeds import seed_roles


@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()

    try:
        seed_roles(db)
        yield

    finally:
        db.close()


app = FastAPI(
    title="SportsIQ AI",
    version="1.0.0",
    lifespan=lifespan,
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

# ==========================
# Authentication
# ==========================
app.include_router(auth_router)

# ==========================
# Dashboard
# ==========================
app.include_router(dashboard_router)

# ==========================
# Football Data
# ==========================
app.include_router(league_router)
app.include_router(team_router)
app.include_router(fixture_router)
app.include_router(standing_router)

# ==========================
# Betting Data
# ==========================
app.include_router(bookmaker_router)

# ==========================
# Bankroll
# ==========================
app.include_router(bankroll_router)
app.include_router(bet_router)