from flask import Blueprint, request, jsonify
from app.controllers.todo_controller import *

api_todo = Blueprint("api_todos", __name__)

@api_todo.route("/", methods=["GET"])
def list_todos():
    todos = get_all_todos()
    return jsonify([{"id": t.id, "text": t.text, "done": t.done} for t in todos])


@api_todo.route("/", methods=["POST"])
def add_todo():
    data = request.get_json() or {}
    text = data.get("text")
    if not text:
        return {"error": "text required"}, 400
    todo = create_todo(text)
    return jsonify({"id": todo.id, "text": todo.text}), 201

@api_todo.route("/<int:todo_id>", methods=["GET"])
def get_single_todo(todo_id):
    todo = get_todo_by_id(todo_id)
    if not todo:
        return {"error": "Todo Not Found."}, 404
    return jsonify({"id": todo_id, "text": todo.text, "done": todo.done})


