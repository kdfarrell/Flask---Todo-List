# app/database.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def init_db(app):

    # Attach db and migrate to the Flask app.
    # Calling this does NOT run migrations; it only initializes the extensions.

    db.init_app(app)
    migrate.init_app(app, db)