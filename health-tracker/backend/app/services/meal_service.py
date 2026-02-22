from app.extensions import db
from app.models import MealLog
from datetime import datetime


class MealService:

    @staticmethod
    def create_meal(user_id, food_name, calories, date):
        meal = MealLog(
            food_name=food_name,
            calories=calories,
            date=datetime.strptime(date, "%Y-%m-%d").date(),
            user_id=user_id
        )

        db.session.add(meal)
        db.session.commit()

        return meal

    @staticmethod
    def get_all_meals(user_id):
        return MealLog.query.filter_by(user_id=user_id).order_by(MealLog.date.desc()).all()

    @staticmethod
    def update_meal(user_id, meal_id, food_name, calories, date):
        meal = MealLog.query.filter_by(id=meal_id, user_id=user_id).first()

        if not meal:
            return None

        meal.food_name = food_name
        meal.calories = calories
        meal.date = datetime.strptime(date, "%Y-%m-%d").date()

        db.session.commit()

        return meal

    @staticmethod
    def delete_meal(user_id, meal_id):
        meal = MealLog.query.filter_by(id=meal_id, user_id=user_id).first()

        if not meal:
            return False

        db.session.delete(meal)
        db.session.commit()

        return True