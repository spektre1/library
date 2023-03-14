"""Initialize the database object. This is eventually attached to the Flask
application after all the models are constructed."""
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def createSchema():
    # sqlite:///library.sqlite
    # sqlite+pysqlite:///:memory:
    engine = create_engine("sqlite:///library.sqlite", echo=True)
