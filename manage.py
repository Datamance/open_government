import os

from flask_script import Manager

from technocracy.webapp import app, database, setup_app
# from technocracy.api import configure_api


api = setup_app(os.getenv('TECHNOCRACY_CONFIG', 'default'), app, database)


manager = Manager(app)


@manager.shell
def make_shell_context():
    return dict(app=app, db=database)


if __name__ == '__main__':
    manager.run()
