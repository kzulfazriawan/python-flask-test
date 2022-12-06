"""create images table

Revision ID: 807f9b59b2d4
Revises: 
Create Date: 2022-12-06 01:40:12.359796

"""
from alembic import op
from src.orm.fields import AutoIncrementId, Character


# revision identifiers, used by Alembic.
revision = '807f9b59b2d4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "images",
        AutoIncrementId("id").field,
        Character("url").field
    )


def downgrade() -> None:
    op.drop_table("images")
