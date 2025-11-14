from app.models.todo import Todo
from app.models.user import User
from app.database import db

# CREATE
def create_todo(text, user_id):
    user = User.query.get(user_id)
    if not user:
        raise ValueError("User not found")
    todo = Todo(text=text, user_id=user_id)
    db.session.add(todo)
    db.session.commit()
    return todo

# READ
def get_todo_by_id(todo_id):
    return Todo.query.get(todo_id)

def get_all_todos():
    return Todo.query.all()

def get_user_todos(user_id):
    user = User.query.get(user_id)
    if not user:
        raise ValueError("User not found")
    return user.todos

# UPDATE
def update_todo_text(todo_id, new_text):
    todo = get_todo_by_id(todo_id)
    if not todo:
        raise ValueError("Todo not found")
    todo.text = new_text
    db.session.commit()
    return todo

def mark_todo_done(todo_id):
    todo = get_todo_by_id(todo_id)
    if not todo:
        raise ValueError("Todo not found")
    todo.mark_done()
    db.session.commit()
    return todo

def mark_todo_undone(todo_id):
    todo = get_todo_by_id(todo_id)
    if not todo:
        raise ValueError("Todo not found")
    todo.mark_undone()
    db.session.commit()
    return todo

# DELETE
def delete_todo(todo_id):
    todo = get_todo_by_id(todo_id)
    if not todo:
        raise ValueError("Todo not found")
    db.session.delete(todo)
    db.session.commit()
    return True
