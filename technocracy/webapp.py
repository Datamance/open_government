from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy_jsonapi import FlaskJSONAPI
import sqlalchemy_jsonapi as sa_jsonapi

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

    print(type(sa_jsonapi.FlaskJSONAPI))
    
    # 3) Get JSON:API compliant endpoints, based on models.
    return FlaskJSONAPI(app, database)
