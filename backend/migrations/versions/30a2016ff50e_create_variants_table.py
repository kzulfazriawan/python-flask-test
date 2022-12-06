"""create variants table

Revision ID: 30a2016ff50e
Revises: 513332507613
Create Date: 2022-12-06 01:40:26.341993

"""
from alembic import op

from src.orm.fields import AutoIncrementId, Character, RichText, CreatedAt, UpdatedAt, Numeric

# revision identifiers, used by Alembic.
revision = '30a2016ff50e'
down_revision = '513332507613'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "variants",
        AutoIncrementId("id").field,
        Numeric("product_id").field,
        Character("name").field,
        Numeric("size", default=1).field,
        Numeric("color", default=1).field,
        RichText("description").field,
        RichText("images", nullable=True).field,
        CreatedAt("created_at").field,
        UpdatedAt("updated_at").field
    )

    op.create_foreign_key(
        "fk_variant_product", "products", "variants", ["id"], ["product_id"]
    )


def downgrade() -> None:
    op.drop_constraint("fk_variant_product", "variants", type_="foreignkey")
    op.drop_table("variants")
