from app.controllers.user_controller import create_user
from app.controllers.todo_controller import create_todo
from app.models.user import User
from app.database import db

def initialize():
    """
    Drops all tables, creates them again, and seeds sample data.
    """
    # Drop and create tables
    db.drop_all()
    db.create_all()

    # Create sample users and todos
    if not User.query.filter_by(username="alice").first():
        alice = create_user("alice", "alicepass")
        create_todo("Buy groceries", alice.id)
        create_todo("Walk the dog", alice.id)

    if not User.query.filter_by(username="bob").first():
        bob = create_user("bob", "bobpass")
        create_todo("Read a book", bob.id)
        create_todo("Do laundry", bob.id)

    db.session.commit()
    print("Database initialized with sample data.")
