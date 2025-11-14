from app.database import db
from sqlalchemy.sql import func

class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    # Foreign key to the user
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __init__(self, text, user_id, done=False):
        self.text = text
        self.user_id = user_id
        self.done = done

    def mark_done(self):
        self.done = True

    def mark_undone(self):
        self.done = False

    def get_json(self):
        return {
            "id": self.id,
            "text": self.text,
            "done": self.done,
            "created_at": self.created_at.isoformat(),
            "user_id": self.user_id,
        }

    def __repr__(self):
        status = "✓" if self.done else "✗"
        return f"[{status}] {self.text}"
