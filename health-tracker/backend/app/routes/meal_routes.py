from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.meal_service import MealService

meal_bp = Blueprint("meals", __name__, url_prefix="/api/meals")


@meal_bp.route("/", methods=["POST"])
@jwt_required()
def create_meal():
    user_id = get_jwt_identity()
    data = request.get_json()

    food_name = data.get("food_name")
    calories = data.get("calories")
    date = data.get("date")

    if not food_name or not calories or not date:
        return jsonify({"error": "All fields required"}), 400

    meal = MealService.create_meal(user_id, food_name, calories, date)

    return jsonify(meal.to_dict()), 201


@meal_bp.route("/", methods=["GET"])
@jwt_required()
def get_meals():
    user_id = get_jwt_identity()

    meals = MealService.get_all_meals(user_id)

    return jsonify([m.to_dict() for m in meals]), 200


@meal_bp.route("/<int:meal_id>", methods=["PUT"])
@jwt_required()
def update_meal(meal_id):
    user_id = get_jwt_identity()
    data = request.get_json()

    updated = MealService.update_meal(
        user_id,
        meal_id,
        data.get("food_name"),
        data.get("calories"),
        data.get("date")
    )

    if not updated:
        return jsonify({"error": "Meal not found"}), 404

    return jsonify(updated.to_dict()), 200


@meal_bp.route("/<int:meal_id>", methods=["DELETE"])
@jwt_required()
def delete_meal(meal_id):
    user_id = get_jwt_identity()

    deleted = MealService.delete_meal(user_id, meal_id)

    if not deleted:
        return jsonify({"error": "Meal not found"}), 404

    return jsonify({"message": "Deleted successfully"}), 200