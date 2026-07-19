from dataclasses import dataclass


@dataclass
class SyncResult:

    created: int = 0
    updated: int = 0
    skipped: int = 0

    def created_one(self):

        self.created += 1

    def updated_one(self):

        self.updated += 1

    def skipped_one(self):

        self.skipped += 1

    def build(
        self,
        message: str,
        total: int,
    ) -> dict:

        return {
            "message": message,
            "created": self.created,
            "updated": self.updated,
            "skipped": self.skipped,
            "total": total,
        }