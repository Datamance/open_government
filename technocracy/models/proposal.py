from ..lib.flaskext import database as db


class Proposal(db.Model):

    # __tablename__ = 'proposals'

    id = db.Column(db.Integer, primary_key=True)
    # Additional fields

    def __repr__(self):
        return 'Proposal {}>'.format(self.id)
