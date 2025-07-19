from flask import Flask
from .extensions.db import db
from .config.config import Config
from .api.webhook import webhook_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(webhook_bp)

    return app
