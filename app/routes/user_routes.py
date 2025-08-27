from flask import Blueprint, request, jsonify
from ..models import User, db

user_bp = Blueprint("user", __name__)

@user_bp.route("/", methods=["POST"])
def create_user():
    """
    Register a new user
    ---
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - username
              - email
              - password
            properties:
              username:
                type: string
              email:
                type: string
              password:
                type: string
    responses:
      201:
        description: User created successfully
    """
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 415

    data = request.get_json()
    if not data or not all(k in data for k in ("username", "email", "password")):
        return jsonify({"error": "Missing required fields"}), 400

    user = User(username=data["username"], email=data["email"], password=data["password"])
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created successfully", "id": user.id}), 201



@user_bp.route("/", methods=["GET"])
def get_users():
    """
    Get all users
    ---
    responses:
      200:
        description: A list of registered users
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              username:
                type: string
              email:
                type: string
    """
    users = User.query.all()
    return jsonify([{"id": u.id, "username": u.username, "email": u.email} for u in users]), 200
