# Lazy SQLAlchemy

A library to wrap sqlalchemy for lazy load of database.

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
db.Model.metadata.create_all(bind=db.engine)
```

## Test

```text
pip install -e .[test]
coverage run --branch --source=src -m unittest discover -v -s tests -t .
```

## License

See LICENSE.
