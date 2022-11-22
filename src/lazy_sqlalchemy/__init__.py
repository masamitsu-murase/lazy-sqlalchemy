from .database import Database


def create_db(*, session_options={}, model_options={}) -> Database:
    """Create Database instance.

    :param session_options: Options passed to sessionmaker.
    :param model_options: Options passed to declarative_base.
    :return: Generated Database instance.
    """
    return Database(session_options=session_options,
                    model_options=model_options)
