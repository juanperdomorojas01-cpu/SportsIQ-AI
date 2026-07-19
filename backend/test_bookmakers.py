import json

from app.services.api_football import APIFootballService

service = APIFootballService()

data = service.get_bookmakers()

print(json.dumps(data, indent=4))