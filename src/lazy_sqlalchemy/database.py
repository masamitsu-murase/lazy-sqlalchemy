from sqlalchemy import create_engine
from sqlalchemy.engine import Engine as BaseEngine
from sqlalchemy.future import Engine as FutureEngine
from sqlalchemy.orm import (DeclarativeMeta, declarative_base, scoped_session,
                            sessionmaker)
from typing import Optional, Union, cast


class Database(object):
    def __init__(self, *, session_options={}, model_options={}) -> None:
        session_factory = sessionmaker(**session_options)
        Session = scoped_session(session_factory)
        self._session = Session
        model = cast(DeclarativeMeta, declarative_base(**model_options))
        model.query = Session.query_property()
        self._model = model
        self._engine = None

    @property
    def session(self) -> scoped_session:
        return self._session

    @property
    def Model(self):
        return self._model

    @property
    def engine(self) -> Optional[Union[BaseEngine, FutureEngine]]:
        return self._engine

    def configure_engine(self, url, **engine_options) -> None:
        """Configure engine of SQLAlchemy.

        :param url: URL for database.
        :param engine_options: options passed to create_engine.
        """
        engine = create_engine(url, **engine_options)
        self._session.configure(bind=engine)
        self._engine = engine
