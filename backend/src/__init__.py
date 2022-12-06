import os

from flask import Flask


ROOT_PATH = os.path.dirname(__file__)
STATIC_PATH = os.path.join(ROOT_PATH, "../static")


class Base:
    app = FLASK = Flask(__name__, static_url_path=STATIC_PATH)
