from app.models.todo import Todo
from app.models.user import User
from app.database import db

def create_todo(user_id, text):
    user = User.query.get(user_id)
    if not user:
        raise ValueError("User not found.")

    if not text or text.strip() == "":
        raise ValueError("Todo text is required.")

    todo = Todo(text=text.strip(), user_id=user_id)
    db.session.add(todo)
    db.session.commit()
    return todo


def get_todo_by_id(todo_id):
    # Important rule: NEVER raise here
    return Todo.query.get(todo_id)


def get_all_todos():
    return Todo.query.all()


def update_todo_text(todo_id, new_text):
    todo = get_todo_by_id(todo_id)
    if not todo:
        raise ValueError("Todo not found.")

    if not new_text or new_text.strip() == "":
        raise ValueError("Todo text is required.")

    todo.text = new_text.strip()
    db.session.commit()
    return todo


def mark_done(todo_id):
    todo = get_todo_by_id(todo_id)
    if not todo:
        raise ValueError("Todo not found.")
    todo.mark_done()
    db.session.commit()
    return todo


def mark_undone(todo_id):
    todo = get_todo_by_id(todo_id)
    if not todo:
        raise ValueError("Todo not found.")

    todo.mark_undone()
    db.session.commit()
    return todo


def delete_todo(todo_id):
    todo = get_todo_by_id(todo_id)
    if not todo:
        raise ValueError("Todo not found.")

    db.session.delete(todo)
    db.session.commit()
    return True
