import json

from app.services.api_football import APIFootballService

service = APIFootballService()

data = service.get_fixtures_by_date("2026-07-20")

print(json.dumps(data, indent=4))
