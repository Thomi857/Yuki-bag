from datetime import datetime
from ..extensions import db


class ExerciseLog(db.Model):
    __tablename__ = "exercise_logs"

    id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String(150), nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    calories_burned = db.Column(db.Integer, nullable=True)
    date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "exercise_name": self.exercise_name,
            "duration_minutes": self.duration_minutes,
            "calories_burned": self.calories_burned,
            "date": self.date.isoformat(),
            "user_id": self.user_id
        }
    

    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)