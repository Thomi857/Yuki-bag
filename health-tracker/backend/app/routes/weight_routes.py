from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.weight_service import WeightService

weight_bp = Blueprint("weights", __name__, url_prefix="/api/weights")


@weight_bp.route("/", methods=["POST"])
@jwt_required()
def create_weight():
    user_id = get_jwt_identity()
    data = request.get_json()

    weight = data.get("weight")
    date = data.get("date")

    if not weight or not date:
        return jsonify({"error": "Weight and date required"}), 400

    weight_log = WeightService.create_weight(user_id, weight, date)

    return jsonify(weight_log.to_dict()), 201


@weight_bp.route("/", methods=["GET"])
@jwt_required()
def get_weights():
    user_id = get_jwt_identity()

    weights = WeightService.get_all_weights(user_id)

    return jsonify([w.to_dict() for w in weights]), 200


@weight_bp.route("/<int:weight_id>", methods=["PUT"])
@jwt_required()
def update_weight(weight_id):
    user_id = get_jwt_identity()
    data = request.get_json()

    weight = data.get("weight")
    date = data.get("date")

    updated = WeightService.update_weight(user_id, weight_id, weight, date)

    if not updated:
        return jsonify({"error": "Weight log not found"}), 404

    return jsonify(updated.to_dict()), 200


@weight_bp.route("/<int:weight_id>", methods=["DELETE"])
@jwt_required()
def delete_weight(weight_id):
    user_id = get_jwt_identity()

    deleted = WeightService.delete_weight(user_id, weight_id)

    if not deleted:
        return jsonify({"error": "Weight log not found"}), 404

    return jsonify({"message": "Deleted successfully"}), 200