"""create products table

Revision ID: 513332507613
Revises: 807f9b59b2d4
Create Date: 2022-12-06 01:40:20.021157

"""
from alembic import op
from src.orm.fields import AutoIncrementId, Character, RichText, CreatedAt, UpdatedAt, RelationshipKey, Numeric

# revision identifiers, used by Alembic.
revision = '513332507613'
down_revision = '807f9b59b2d4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "products",
        AutoIncrementId("id").field,
        Character("name").field,
        RichText("description").field,
        RichText("images", nullable=True).field,
        Numeric("logo_id").field,
        CreatedAt("created_at").field,
        UpdatedAt("updated_at").field
    )

    op.create_foreign_key(
        "fk_product_logo_id", "images", "products", ["id"], ["logo_id"]
    )


def downgrade() -> None:
    op.drop_constraint("fk_product_logo_id", "products", type_="foreignkey")
    op.drop_table("products")
