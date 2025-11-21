from app.models.user import User
from app.database import db

# CREATE
def create_user(username, password):
    if User.query.filter_by(username=username).first():
        raise ValueError("Username already exists")
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return user

# READ
def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_all_users():
    return User.query.all()

def get_user_todos(user_id):
    user = User.query.get(user_id)
    if not user:
        raise ValueError("User not found.")
    return user.todos

# UPDATE
def update_username(user_id, new_username):
    user = get_user_by_id(user_id)
    if not user:
        raise ValueError("User not found")
    user.username = new_username
    db.session.commit()
    return user

def update_password(user_id, new_password):
    user = get_user_by_id(user_id)
    if not user:
        raise ValueError("User not found")
    user.set_password(new_password)
    db.session.commit()
    return user

# DELETE
def delete_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        raise ValueError("User not found")
    db.session.delete(user)
    db.session.commit()
    return True
