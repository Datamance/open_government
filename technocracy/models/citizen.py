from ..webapp import database as db
from .mixins import User


class Citizen(User, db.Model):
    """
    The basic model for a citizen in your government.
    """
    pass
