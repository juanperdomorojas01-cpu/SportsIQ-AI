from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Bienvenido a SportsIQ AI"
    }


@router.get("/health")
def health():
    return {
        "status": "ok"
    }