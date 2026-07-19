class SyncValidator:

    @staticmethod
    def has_required_fields(
        item: dict,
        *fields: str,
    ) -> bool:

        for field in fields:

            value = item.get(field)

            if value is None:
                return False

            if isinstance(value, str) and not value.strip():
                return False

        return True