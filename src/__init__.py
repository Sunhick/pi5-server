from flask import Flask
from .config import Config
from .routes import register_routes
import logging

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Logging
    logging.basicConfig(level=logging.INFO)
    app.logger = logging.getLogger(__name__)

    # Register routes
    register_routes(app)

    return app
