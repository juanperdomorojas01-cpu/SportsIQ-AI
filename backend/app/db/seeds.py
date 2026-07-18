from sqlalchemy.orm import Session

from app.models.role import Role


def seed_roles(db: Session):

    roles = [
        {
            "name": "ADMIN",
            "description": "Administrador del sistema",
        },
        {
            "name": "USER",
            "description": "Usuario de la plataforma",
        },
    ]

    for role in roles:

        exists = (
            db.query(Role)
            .filter(Role.name == role["name"])
            .first()
        )

        if not exists:

            db.add(
                Role(
                    name=role["name"],
                    description=role["description"],
                )
            )

    db.commit()