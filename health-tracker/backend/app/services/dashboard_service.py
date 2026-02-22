from app.models import WeightLog, MealLog
from app.extensions import db
from sqlalchemy import func
from datetime import datetime


class DashboardService:

    @staticmethod
    def get_summary(user_id, start_date=None, end_date=None):

        weight_query = WeightLog.query.filter_by(user_id=user_id)
        meal_query = MealLog.query.filter_by(user_id=user_id)

        if start_date and end_date:
            start = datetime.strptime(start_date, "%Y-%m-%d").date()
            end = datetime.strptime(end_date, "%Y-%m-%d").date()

            weight_query = weight_query.filter(
                WeightLog.date.between(start, end)
            )

            meal_query = meal_query.filter(
                MealLog.date.between(start, end)
            )

        total_calories = meal_query.with_entities(
            func.coalesce(func.sum(MealLog.calories), 0)
        ).scalar()

        average_weight = weight_query.with_entities(
            func.avg(WeightLog.weight)
        ).scalar()

        latest_weight = weight_query.order_by(
            WeightLog.date.desc()
        ).first()

        total_meals = meal_query.count()
        total_weight_entries = weight_query.count()

        return {
            "total_calories": total_calories or 0,
            "average_weight": round(average_weight, 2) if average_weight else None,
            "latest_weight": latest_weight.weight if latest_weight else None,
            "total_meals": total_meals,
            "total_weight_entries": total_weight_entries
        }