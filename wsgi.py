from main import create_app
from app.database import init_db
from app.controllers.initialize import initialize
from app.controllers.user_controller import *

app = create_app()
init_db(app)

# CLI command
@app.cli.command("init", help="Creates and initializes the database with sample data")
def init():
    initialize()


# List all users
@app.cli.command("list-users", help="Print all users in the database")
def list_users():
    users = get_all_users()
    if not users:
        print("No users found.")
        return
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}")