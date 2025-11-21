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
    user_id = data.get("user_id")

    if not user_id:
        return {"error": "user_id required"}, 400
    
    if not text:
        return {"error": "text required"}, 400

    try:
        todo = create_todo(user_id, text)
    except ValueError as e:
        return {"error": str(e)}, 404 

    return jsonify({
        "id": todo.id,
        "text": todo.text,
        "done": todo.done,
        "user_id": todo.user_id,
        "created_at": todo.created_at,
    }), 201


@api_todo.route("/<int:todo_id>", methods=["GET"])
def get_single_todo(todo_id):
    todo = get_todo_by_id(todo_id)
    if not todo:
        return {"error": "Todo Not Found."}, 404
    return jsonify({"id": todo_id, "text": todo.text, "done": todo.done})


@api_todo.route("/<int:todo_id>", methods=["PUT"])
def update_todo_route(todo_id):
    data = request.get_json() or {}
    new_text = data.get("text")
    if not new_text:
        return {"error": "text required"}, 400

    todo = update_todo_text(todo_id, new_text)
    if not todo:
        return {"error": "Todo not found"}, 404

    return jsonify({"id": todo.id, "text": todo.text, "done": todo.done})


@api_todo.route("/<int:todo_id>", methods=["DELETE"])
def delete_todo_route(todo_id):
    deleted = delete_todo(todo_id)
    if not deleted:
        return {"Error": "Todo not found"}, 404
    return {"message": "Todo Deleted."}


@api_todo.route("/<int:todo_id>/done", methods=["PATCH"])
def mark_todo_done(todo_id):
    try:
        todo = mark_done(todo_id)
    except ValueError as e:
        return {"error": {e}}, 40
    return jsonify({"id": todo.id, "text": todo.text, "done": todo.done})


@api_todo.route("/<int:todo_id>/undone", methods=["PATCH"])
def mark_todo_undone(todo_id):
    try:
        todo = mark_undone(todo_id)
    except ValueError as e:
        return {"error": {e}}, 404

    return jsonify({"id": todo.id,  "text": todo.text, "done": todo.done})
