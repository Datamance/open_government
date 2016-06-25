from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS
from sqlalchemy_jsonapi import FlaskJSONAPI

from config import config

# 1) create the flask application.
app = Flask(__name__)

# 2) Set up the database. We can now import this anywhere.
database = SQLAlchemy(app)


def setup_app(config_name, app, database):
	"""Creates a JSON:API compliant REST application."""

    # 1) Set up appropriate app configs.
    app.config.from_object(config[config_name])

    # 2) Set up CORS.
    CORS(app)

    # 3) set up JSON:API compliant endpoints, based on models.
    api = FlaskJSONAPI(app, database)

    # 5) Give up all the goodies.
    return api
