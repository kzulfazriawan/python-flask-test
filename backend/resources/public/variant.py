from models.variants import Variants as _Model
from resources import Resource as _Resource
from src.orm.model import to_list, to_dict


class Variant(_Resource):
    model = _Model()

    def __init__(self):
        super(Variant, self).__init__()

    def get(self):
        get_all = self.model.select().all()
        return self.response.json(to_list(get_all), status_code=200)

    def delete(self, id):
        self.model.select().filter(id=id).delete()
        return self.response.json({}, status_code=200)

    def put(self, id):
        self.request.parsing()
        update = self.model.select().filter(id=id).edit(self.request.parse.form)

        return self.response.json(to_dict(update), status_code=200)

    def post(self):
        validation = self.request.validation(
            name="required",
            product_id="required",
            description="required",
            size="required",
            color="required",
            images="required",
        )

        if "errors" in validation:
            return validation

        saved = self.model.create(**self.request.parse.form)

        return self.response.json({"name": saved.name, "id": saved.id}, status_code=200)
