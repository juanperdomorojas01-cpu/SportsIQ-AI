from sqlalchemy.orm import Session

from app.models.bet_type import BetType
from app.repositories.bet_type_repository import BetTypeRepository
from app.services.api_football import APIFootballService


class BetTypeService:

    def __init__(self, db: Session):

        self.repository = BetTypeRepository(db)
        self.api = APIFootballService()

    def test_bet_types(self):

        return self.api.get_bets()

    def sync_bet_types(self):

        data = self.api.get_bets()

        created = 0
        updated = 0
        skipped = 0

        for item in data["response"]:

            api_id = item.get("id")
            name = item.get("name")

            if api_id is None or not name:
                skipped += 1
                continue

            bet_type = self.repository.get_by_api_id(api_id)

            if bet_type is None:

                bet_type = BetType(
                    api_id=api_id,
                    name=name,
                    description=None,
                    is_active=True,
                )

                self.repository.add(bet_type)
                created += 1

            else:

                bet_type.name = name
                bet_type.is_active = True

                self.repository.commit()
                updated += 1

        return {
            "message": "Bet Types sincronizados correctamente.",
            "created": created,
            "updated": updated,
            "skipped": skipped,
            "total": self.repository.count(),
        }