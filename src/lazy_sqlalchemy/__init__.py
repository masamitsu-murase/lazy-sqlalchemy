from sqlalchemy import create_engine
from sqlalchemy.orm import (DeclarativeMeta, declarative_base, scoped_session,
                            sessionmaker)

__all__ = ["create_db"]


class Database(object):
    def __init__(self, *, session_options={}):
        session_factory = sessionmaker(**session_options)
        Session = scoped_session(session_factory)
        self._session = Session
        self._model: DeclarativeMeta = declarative_base()
        self._model.query = Session.query_property()
        self._engine = None

    @property
    def session(self):
        return self._session

    @property
    def Model(self):
        return self._model

    @property
    def engine(self):
        return self._engine

    def configure_engine(self, url, **engine_options):
        engine = create_engine(url, **engine_options)
        self._session.configure(bind=engine)
        self._engine = engine


def create_db(*, session_options={}) -> Database:
    return Database(session_options=session_options)
