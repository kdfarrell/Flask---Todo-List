# app/__init__.py
from flask import Flask
from .database import init_db

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize DB (and migration wiring, if present)
    init_db(app)

    # Register blueprints
    from .views.api.todo_views import api_todo
    app.register_blueprint(api_todo, url_prefix="/api/todos")

    return app