from sqlalchemy import ForeignKeyConstraint, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from src.orm.fields import AutoIncrementId, Character, RichText, CreatedAt, UpdatedAt, RelationshipKey
from src.orm.model import Model, Queries


class Products(Model, Queries):
    __tablename__ = "products"

    id = AutoIncrementId().field
    name = Character().field
    description = RichText().field
    images = RichText(nullable=True).field
    logo_id = Column(Integer, ForeignKey("images.id", ondelete="CASCADE"))
    created_at = CreatedAt().field
    updated_at = UpdatedAt().field
