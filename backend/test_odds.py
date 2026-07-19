import json

from app.services.api_football import APIFootballService

service = APIFootballService()

fixture_id = 1508813  # FH Hafnarfjordur vs Breidablik

data = service.get_odds(fixture_id)

print(json.dumps(data, indent=4))