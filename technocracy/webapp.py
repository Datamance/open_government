from flask import Flask
from flask_cors import CORS

from config import config

from .lib.flaskext import api, database


def setup_app(config_name):
    """
    Creates a JSON:API compliant REST application.

    :param config_name str: String name of the config.
    :param app: The application.
    :param database: SQLAlchemy database.
    """
    # Setup Flask App
    app = Flask('open_government')

    # Load Configurations
    app.config.from_object(config[config_name])

    # Initialize extensions
    database.init_app(app)
    CORS(app)
    api.init_app(app, database)

    return app
