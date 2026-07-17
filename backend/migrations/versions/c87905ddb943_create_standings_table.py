"""create standings table

Revision ID: c87905ddb943
Revises: b180a96f89e4
Create Date: 2026-07-06

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers
revision: str = "c87905ddb943"
down_revision: Union[str, Sequence[str], None] = "b180a96f89e4"
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_table(
        "standings",

        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True
        ),

        sa.Column(
            "league_id",
            sa.Integer(),
            sa.ForeignKey("leagues.id"),
            nullable=False
        ),

        sa.Column(
            "team_id",
            sa.Integer(),
            sa.ForeignKey("teams.id"),
            nullable=False
        ),

        sa.Column(
            "season",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "position",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "points",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "played",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "win",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "draw",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "lose",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "goals_for",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "goals_against",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "goal_difference",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "form",
            sa.String(length=30),
            nullable=True
        )
    )


def downgrade() -> None:

    op.drop_table("standings")