from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.dashboard_service import DashboardService

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/api/dashboard")


@dashboard_bp.route("/summary", methods=["GET"])
@jwt_required()
def get_dashboard_summary():
    user_id = get_jwt_identity()

    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    summary = DashboardService.get_summary(
        user_id,
        start_date,
        end_date
    )

    return jsonify(summary), 200