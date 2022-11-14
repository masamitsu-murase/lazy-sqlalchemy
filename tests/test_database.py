from sqlalchemy import Column, Integer, String
from sqlalchemy.exc import OperationalError
import unittest
import lazy_sqlalchemy


class DatabaseTestCase(unittest.TestCase):
    def test_create_db_with_autoflush(self):
        db = lazy_sqlalchemy.create_db(
            session_options=dict(autoflush=True))

        class User(db.Model):
            __tablename__ = "users"
            id = Column("id", Integer, primary_key=True)
            name = Column("name", String(50), nullable=False, unique=True)

        db.configure_engine("sqlite:///:memory:")
        db.Model.metadata.create_all(bind=db.engine)

        self.assertEqual(User.query.count(), 0)
        user = User(name="sample")
        db.session.add(user)
        self.assertEqual(User.query.count(), 1)
        db.session.commit()
        self.assertEqual(User.query.count(), 1)

        db.session.remove()
        db.configure_engine("sqlite:///:memory:")
        with self.assertRaises(OperationalError):
            self.assertEqual(User.query.count(), 0)
        db.Model.metadata.create_all(bind=db.engine)
        self.assertEqual(User.query.count(), 0)

    def test_create_db_without_autoflush(self):
        db = lazy_sqlalchemy.create_db(
            session_options=dict(autoflush=False))

        class User(db.Model):
            __tablename__ = "users"
            id = Column("id", Integer, primary_key=True)
            name = Column("name", String(50), nullable=False, unique=True)

        db.configure_engine("sqlite:///:memory:")
        db.Model.metadata.create_all(bind=db.engine)

        self.assertEqual(User.query.count(), 0)
        user = User(name="sample")
        db.session.add(user)
        self.assertEqual(User.query.count(), 0)
        db.session.commit()
        self.assertEqual(User.query.count(), 1)
