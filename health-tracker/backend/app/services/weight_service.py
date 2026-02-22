from app.extensions import db
from app.models import WeightLog
from datetime import datetime


class WeightService:

    @staticmethod
    def create_weight(user_id, weight, date):
        weight_log = WeightLog(
            weight=weight,
            date=datetime.strptime(date, "%Y-%m-%d").date(),
            user_id=user_id
        )

        db.session.add(weight_log)
        db.session.commit()

        return weight_log

    @staticmethod
    def get_all_weights(user_id):
        return WeightLog.query.filter_by(user_id=user_id).order_by(WeightLog.date.desc()).all()

    @staticmethod
    def update_weight(user_id, weight_id, weight, date):
        weight_log = WeightLog.query.filter_by(id=weight_id, user_id=user_id).first()

        if not weight_log:
            return None

        weight_log.weight = weight
        weight_log.date = datetime.strptime(date, "%Y-%m-%d").date()

        db.session.commit()

        return weight_log

    @staticmethod
    def delete_weight(user_id, weight_id):
        weight_log = WeightLog.query.filter_by(id=weight_id, user_id=user_id).first()

        if not weight_log:
            return False

        db.session.delete(weight_log)
        db.session.commit()

        return True