from flask import Blueprint, request, jsonify
from app.controllers.todo_controller import create_todo, get_all_todos, mark_done

api_todo = Blueprint("api_todos", __name__)

@api_todo.route("/", methods=["POST"])
def add_todo():
    data = request.get_json() or {}
    text = data.get("text")
    if not text:
        return {"error": "text required"}, 400
    todo = create_todo(text)
    return jsonify({"id": todo.id, "text": todo.text}), 201

@api_todo.route("/", methods=["GET"])
def list_todos():
    todos = get_all_todos()
    return jsonify([{"id": t.id, "text": t.text, "done": t.done} for t in todos])