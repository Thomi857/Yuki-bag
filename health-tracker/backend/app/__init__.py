from flask import Flask
from flask_cors import CORS
from .extensions import db, jwt, migrate
from .config import DevelopmentConfig, ProductionConfig
import os

def create_app():
    app = Flask(__name__)

    env = os.getenv("FLASK_ENV", "development")
    if env == "production":
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    CORS(app, origins=app.config.get("CORS_ORIGINS", "*"))

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return {"error": "Invalid token"}, 401

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return {"error": "Authorization token required"}, 401

    from app import models

    # Register ALL blueprints here
    from app.routes.auth_routes import auth_bp
    from app.routes.dashboard_routes import dashboard_bp
    from app.routes.weight_routes import weight_bp
    from app.routes.meal_routes import meal_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(weight_bp)
    app.register_blueprint(meal_bp)

    return app