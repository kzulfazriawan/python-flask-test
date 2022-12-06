import os

from flask_cors import CORS

from resources.routes import Routes
from src.crawler import walk


class Main(Routes):
    def __init__(self):
        super(Main, self).__init__()

    def resources(self):
        for k, v in walk('resources', 'public', 'resources/public').items():
            url = k.replace('resources.public.', '').split('.')[:-1]
            url = os.path.join(*url) if len(url) > 1 else ''

            self.resource(v, str(url))

    def run(self):
        self.app.run(port=8000, debug=True, host="0.0.0.0")


if __name__ == "__main__":
    main = Main()
    main.app.config['WTF_CSRF_ENABLED'] = False
    cors = CORS(main.app, origins="*")
    with main.app.test_request_context():
        main.resources()
        main.run()
