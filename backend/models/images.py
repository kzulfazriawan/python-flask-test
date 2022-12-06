from src.orm.fields import AutoIncrementId, Character
from src.orm.model import Model, Queries


class Images(Model, Queries):
    __tablename__ = "images"

    id = AutoIncrementId().field
    url = Character().field
