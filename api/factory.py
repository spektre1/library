"""Factory that constructs the Flask application, assembling all the
components."""

import connexion
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from containers import Container
# from db import createSchema

def register_apis(connexionApp:connexion.App) -> None:
    """Public facing APIs managed by Connexion."""
    connexionApp.add_api('api.yaml')


def register_blueprints(app:Flask) -> None:
    """Admin UI managed by Flask Blueprints."""
    from views import admin_bp
    app.register_blueprint(admin_bp)


def setup_db(app:Flask, db:SQLAlchemy) -> None:
    """SQLAlchemy manages DB."""
    from models import db
    db.init_app(app)
    # createSchema()
    # Will need this for perm db:
    # migrate = Migrate(app, db)
    # with app.app_context():  # Register DB Models
    #     db.drop_all()  #TODO: Get rid of this for perm db
    #     db.create_all()


def create_app(db:SQLAlchemy) -> Flask:
    container = Container()
    connexionApp = connexion.App(__name__, specification_dir='openapi/')
    register_apis(connexionApp)
    app = connexionApp.app
    app.container = container
    register_blueprints(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
    # setup_db(app, db)
    print(f"Database: {db}")
    return app
