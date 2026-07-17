"""create fixtures table

Revision ID: b180a96f89e4
Revises: e8f81988d8e9
Create Date: 2026-07-06
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers
revision: str = "b180a96f89e4"
down_revision: Union[str, Sequence[str], None] = "e8f81988d8e9"
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_table(
        "fixtures",

        sa.Column("id", sa.Integer(), primary_key=True),

        sa.Column(
            "api_id",
            sa.Integer(),
            nullable=False,
            unique=True
        ),

        sa.Column(
            "referee",
            sa.String(length=150),
            nullable=True
        ),

        sa.Column(
            "timezone",
            sa.String(length=50),
            nullable=False
        ),

        sa.Column(
            "date",
            sa.DateTime(),
            nullable=False
        ),

        sa.Column(
            "timestamp",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "status",
            sa.String(length=30),
            nullable=False
        ),

        sa.Column(
            "league_id",
            sa.Integer(),
            sa.ForeignKey("leagues.id"),
            nullable=False
        ),

sa.Column(
    "home_team_id",
    sa.Integer(),
    sa.ForeignKey("teams.id"),
    nullable=False
),

sa.Column(
    "away_team_id",
    sa.Integer(),
    sa.ForeignKey("teams.id"),
    nullable=False
),

        sa.Column(
            "home_goals",
            sa.Integer(),
            nullable=True
        ),

        sa.Column(
            "away_goals",
            sa.Integer(),
            nullable=True
        ),
    )


def downgrade() -> None:

    op.drop_table("fixtures")