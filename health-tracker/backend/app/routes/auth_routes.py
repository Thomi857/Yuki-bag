from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.auth_service import AuthService
from app.models import User

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "All fields are required"}), 400

    user, error = AuthService.register(username, email, password)

    if error:
        return jsonify({"error": error}), 400

    return jsonify({
        "message": "User registered successfully",
        "user": user.to_dict()
    }), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    token, error = AuthService.login(email, password)

    if error:
        return jsonify({"error": error}), 401

    return jsonify({
        "message": "Login successful",
        "access_token": token
    }), 200


@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def get_current_user():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    return jsonify(user.to_dict()), 200