import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    PREFERRED_URL_SCHEME = ('http')


# TODO(rico): follow up with sqlalchemy-jsonapi fellow to make sure
# he uses SQLALCHEMY_DATABASE_URI in the future

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'TECHNOCRACY_PRODUCTION_DATABASE_URI'
    )


class DevelopmentConfig(Config):
    DEBUG = True
    SERVER_NAME = 'localhost:5000'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'TECHNOCRACY_DEVELOPMENT_DATABASE_URI'
    )


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'TECHNOCRACY_TESTING_DATABASE_URI'
    )


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig,
}
