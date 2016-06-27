from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # declarative_base
from flask_cors import CORS
from sqlalchemy_jsonapi import FlaskJSONAPI

from config import config

# 1) create the flask application.
app = Flask(__name__)

# 2) Set up the database. We can now import this anywhere.
database = SQLAlchemy(app)

# Declarative base needs to be hooked up to the correct engine...
# OrmBase = declarative_base()


def setup_app(config_name, app, database):
    """
    Creates a JSON:API compliant REST application.

    :param config_name str: String name of the config.
    :param app: The application.
    :param database: SQLAlchemy database.
    """
    # 0) Import models. SQLAlchemy requires this during app initialization.
    from .models import (Citizen, Proposal)

    # 1) Set up appropriate app configs.
    app.config.from_object(config[config_name])

    # 2) Set up CORS.
    CORS(app)

    # 3) Get JSON:API compliant endpoints, based on models.
    return FlaskJSONAPI(app, database)
