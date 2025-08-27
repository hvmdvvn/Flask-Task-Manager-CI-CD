from flask import Blueprint, request, jsonify
from ..models import Task, db

task_bp = Blueprint("task", __name__)

@task_bp.route("/", methods=["GET"])
def get_tasks():
    """
    Get all tasks
    ---
    responses:
      200:
        description: List of tasks
        schema:
          type: array
          items:
            type: object
            properties:
              id: {type: integer}
              title: {type: string}
              description: {type: string}
              due_date: {type: string, format: date-time}
              completed: {type: boolean}
              user_id: {type: integer}
    """
    tasks = Task.query.all()
    return jsonify([t.to_dict() for t in tasks]), 200


@task_bp.route("/", methods=["POST"])
def create_task():
    """
    Create a new task
    ---
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - title
              - user_id
            properties:
              title:
                type: string
              description:
                type: string
              user_id:
                type: integer
    responses:
      201:
        description: Task created successfully
    """
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 415

    data = request.get_json()
    if not data or "title" not in data or "user_id" not in data:
        return jsonify({"error": "Title and user_id required"}), 400

    task = Task(
        title=data["title"],
        description=data.get("description"),
        user_id=data["user_id"]
    )
    db.session.add(task)
    db.session.commit()

    return jsonify(task.to_dict()), 201



@task_bp.route("/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    """
    Update a task
    ---
    parameters:
      - in: path
        name: task_id
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            title: {type: string}
            description: {type: string}
            completed: {type: boolean}
    responses:
      200:
        description: Task updated
      404:
        description: Task not found
    """
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    if "title" in data: task.title = data["title"]
    if "description" in data: task.description = data["description"]
    if "completed" in data: task.completed = data["completed"]

    db.session.commit()
    return jsonify(task.to_dict()), 200


@task_bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """
    Delete a task
    ---
    parameters:
      - in: path
        name: task_id
        type: integer
        required: true
    responses:
      200:
        description: Task deleted
      404:
        description: Task not found
    """
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"}), 200
