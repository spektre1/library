"""Initialize the database object. This is eventually attached to the Flask
application after all the models are constructed."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase


db = SQLAlchemy()

class Base(DeclarativeBase):
    pass

def createSchema():
    # sqlite:///library.sqlite
    # sqlite+pysqlite:///:memory:
    engine = create_engine("sqlite:///library.sqlite", echo=True)
    Base.metadata.create_all(engine)