from ..lib.flaskext import database as db


class Citizen(db.Model):

    # __tablename__ = 'citizens'

    id = db.Column(db.Integer, primary_key=True)
    # Additional fields

    def __repr__(self):
        return 'Citizen {}>'.format(self.id)
