from fastapi import FastAPI

app = FastAPI(
    title="SportsIQ AI",
    version="0.1.0",
    description="API para análisis y predicción deportiva."
)

@app.get("/")
def root():
    return {
        "name": "SportsIQ AI",
        "version": "0.1.0",
        "status": "running",
        "message": "¡Bienvenido a SportsIQ AI!"
    }
