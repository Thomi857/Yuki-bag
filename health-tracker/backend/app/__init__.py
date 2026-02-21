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

    CORS(app, origins=app.config["CORS_ORIGINS"])

    return app