# Lazy SQLAlchemy

A library to wrap sqlalchemy for lazy load of database.

This tiny library is baesd on the functionality of [`sessionmaker`](https://docs.sqlalchemy.org/en/14/orm/session_api.html#session-and-sessionmaker).  
According to the document, we can bind an engine to `Session` after we create `Session` instance.

## Usage

```python
from sqlalchemy import Column, Integer, String
import lazy_sqlalchemy


db = lazy_sqlalchemy.create_db()

class User(db.Model):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(50), nullable=False, unique=True)

# You can configure database URI after you create db instance.
db.configure_engine("sqlite:///:memory:")

# You can invoke any SQL statements.
db.Model.metadata.create_all(bind=db.engine)
u = User(name="Murase")
db.session.add(u)
db.session.commit()
```

Note that you can call `db.configure_engine` with URL for your database *after* you define `User` class.  
Therefore, you can replace database URL easily for test.

## Test

```text
pip install -e .[test]
coverage run --branch --source=src -m unittest discover -v -s tests -t .
```

## License

See LICENSE.
