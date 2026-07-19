import json

from app.services.api_football import APIFootballService

service = APIFootballService()

data = service.get_players(
    team_id=33,      # Manchester United
    season=2025,
)

print(json.dumps(data, indent=4))