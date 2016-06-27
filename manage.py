import os

from flask_script import Manager, Server, prompt_bool

from technocracy.webapp import setup_app, api, database
# from technocracy.api import configure_api


app = setup_app(os.getenv('TECHNOCRACY_CONFIG', 'default'))

manager = Manager(app)

manager.add_command('runlocal', Server(host='localhost', port=5000))


@manager.shell
def make_shell_context():
    """This saves quite a few imports."""
    return dict(app=app, db=database, api=api)


@manager.command
def init_db():
    """Initializes the database.

    TODO(rico): Create the databases conditionally, or with a prompt:
        "There's no database currently" and then create dbs based on
        db config settings.
    """
    from technocracy.models import (
        Citizen, Proposal)

    database.create_all()


@manager.command
def drop_tables():
    """Drops all the tables."""
    if prompt_bool('You sure you wanna destroy the current government?'):
        database.drop_all()


if __name__ == '__main__':
    manager.run()
