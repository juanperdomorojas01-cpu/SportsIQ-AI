import json
import httpx

from app.core.config import settings

headers = {
    "x-apisports-key": settings.API_FOOTBALL_KEY
}

response = httpx.get(
    "https://v3.football.api-sports.io/status",
    headers=headers,
    timeout=30
)

print("STATUS CODE:", response.status_code)
print(json.dumps(response.json(), indent=4))