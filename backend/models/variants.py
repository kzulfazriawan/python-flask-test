from src.orm.fields import AutoIncrementId, Character, RichText, CreatedAt, UpdatedAt, RelationshipKey, Numeric
from src.orm.model import Model, Queries


class Variants(Model, Queries):
    __tablename__ = "variants"

    id = AutoIncrementId()
    name = Character().field
    product_id = RelationshipKey("products.id").field
    description = RichText().field
    images = RichText(nullable=True).field
    size = Numeric().field
    color = Numeric().field
    created_at = CreatedAt().field
    updated_at = UpdatedAt().field
