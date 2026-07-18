from sqlalchemy.orm import Session

from app.models.bookmaker import Bookmaker
from app.repositories.bookmaker_repository import BookmakerRepository
from app.services.api_football import APIFootballService


class BookmakerService:

    def __init__(self, db: Session):

        self.repository = BookmakerRepository(db)
        self.api = APIFootballService()

    def sync_bookmakers(self):

        data = self.api.get_bookmakers()

        created = 0
        updated = 0
        skipped = 0

        for item in data["response"]:

            api_id = item.get("id")
            name = item.get("name")

            # Ignorar registros inválidos
            if api_id is None or not name:
                skipped += 1
                continue

            bookmaker = self.repository.get_by_api_id(api_id)

            if bookmaker is None:

                bookmaker = Bookmaker(
                    api_id=api_id,
                    name=name,
                    website=None,
                    logo=None,
                    is_active=True,
                )

                self.repository.add(bookmaker)

                created += 1

            else:

                bookmaker.name = name
                bookmaker.is_active = True

                self.repository.commit()

                updated += 1

        return {
            "message": "Bookmakers sincronizados correctamente.",
            "created": created,
            "updated": updated,
            "skipped": skipped,
            "total": self.repository.count(),
        }

    def test_bookmakers(self):

        data = self.api.get_bookmakers()

        for item in data["response"]:

            if item.get("id") == 37:
                return item

        return {
            "message": "Bookmaker con id 37 no encontrado."
        }