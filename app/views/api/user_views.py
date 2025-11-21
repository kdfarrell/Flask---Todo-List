from flask import Blueprint, request, jsonify
from app.controllers.user_controller import *
from app.controllers.todo_controller import list_todos


api_user = Blueprint("api_user", __name__)

@api_user.route("/", methods=["GET"])
def list_users():
    users = get_all_users()
    return jsonify([{"id": user.id, "name": user.username} for user in users])

@api_user.route("/<int:user_id>", methods=["GET"])
def list_user_todos(user_id):
    try:
        user_todos = get_user_todos(user_id)
        return jsonify([{"id": todo.id, "text": todo.text, "created_at": todo.created_at} for todo in user_todos])
    except ValueError as e:
        return {"error": str(e)}, 404