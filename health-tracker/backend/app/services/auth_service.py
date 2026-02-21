from app.extensions import db
from app.models import User
from flask_jwt_extended import create_access_token


class AuthService:

    @staticmethod
    def register(username, email, password):
        existing_user = User.query.filter(
            (User.email == email) | (User.username == username)
        ).first()

        if existing_user:
            return None, "User with that email or username already exists"

        user = User(username=username, email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return user, None

    @staticmethod
    def login(email, password):
        user = User.query.filter_by(email=email).first()

        if not user or not user.check_password(password):
            return None, "Invalid credentials"

        access_token = create_access_token(identity=user.id)

        return access_token, None