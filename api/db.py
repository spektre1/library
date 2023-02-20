"""Initialize the database object. This is eventually attached to the Flask
application after all the models are constructed."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
