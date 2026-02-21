from flask import Flask
from flask_cors import CORS
from .extensions import db, jwt, migrate
from .config import DevelopmentConfig, ProductionConfig
import os
from app import models


def create_app():
    # 1. Create the app object FIRST
    app = Flask(__name__)

    # 2. Load configurations
    env = os.getenv("FLASK_ENV", "development")
    if env == "production":
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    # 3. Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    CORS(app, origins=app.config.get("CORS_ORIGINS", "*"))

    # 4. JWT Callbacks (Indentation fixed)
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return {"error": "Invalid token"}, 401

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return {"error": "Authorization token required"}, 401

    # 5. IMPORTANT: Import models here so Migrations can see them
    from app import models 

    # 6. Register Blueprints (Now 'app' exists, so this works)
    from app.routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp)

    return app