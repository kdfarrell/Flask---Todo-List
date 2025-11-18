import click
from main import create_app
from app.database import init_db
from app.controllers.initialize import initialize
from app.controllers.user_controller import *
from app.controllers.todo_controller import *

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



# Todo commands
@app.cli.command("list-todos", help="List all todos in the database")
def list_todos():
    todos = get_all_todos()
    if not todos:
        print("No todos found.")
        return
    for todo in todos:
        print(f"ID: {todo.id}\nTodo: {todo.text}\nDate Created: {todo.created_at}\nCompleted: {todo.done}\n")


@app.cli.command("todo", help="Get a single todo by ID")
@click.argument("todo_id")
def get_single(todo_id):
    with app.app_context():
        todo = get_todo_by_id(todo_id)
        if not todo:
            print("Todo not found.")
        else:
            print(f"ID: {todo.id}")
            print(f"Text: {todo.text}")
            print(f"Done: {todo.done}")


@app.cli.command("update-todo", help="Update a todo's text by ID")
@click.argument("todo_id")
@click.argument("new_text")
def update_todo(todo_id, new_text):
    updated_todo = update_todo_text(todo_id, new_text)

    if not updated_todo:
        print("Todo not found.")
        return

    print("Todo updated:")
    print(f"ID: {updated_todo.id}\nText: {updated_todo.text}\nDone: {updated_todo.done}")
