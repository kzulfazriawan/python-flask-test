from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from alembic.config import Config

_config = Config()
_engine = create_engine(_config.get_main_option("sqlalchemy.url", "mysql://myuser:mypasswd@db/flask_project"))


def session(direct=False):
    """
    Build a session from the engine database

    :param direct:
    :return: session or direct engine
    """

    if not direct:
        session_ng = sessionmaker(bind=_engine, expire_on_commit=True)
        return session_ng()
    else:
        return _engine.begin()
