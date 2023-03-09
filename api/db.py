"""Initialize the database object. This is eventually attached to the Flask
application after all the models are constructed."""
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine
# engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

#db = SQLAlchemy(engine=engine)
db = SQLAlchemy()
