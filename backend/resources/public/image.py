import os.path

from werkzeug.utils import secure_filename

from models.images import Images as _Model
from resources import Resource as _Resource
from src import STATIC_PATH
from src.orm.model import to_dict, to_list


class Image(_Resource):
    model = _Model()

    def __init__(self):
        super(Image, self).__init__()

    def get(self):
        get_all = self.model.select().all()
        return self.response.json(to_list(get_all), status_code=200)

    def delete(self, id):
        self.model.select().filter(id=id).delete()
        return self.response.json({}, status_code=200)

    def post(self):
        validation = self.request.validation(
            upload="required"
        )

        if "errors" in validation:
            return validation

        upload = self.request.parse.file["upload"][0]
        filename = secure_filename(upload.filename)
        upload.save(os.path.join(STATIC_PATH, filename))
        saved = self.model.create(url=filename)

        return self.response.json({"uploaded": saved.url, "id": saved.id}, status_code=200)
