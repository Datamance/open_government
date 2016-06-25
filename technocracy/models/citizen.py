from .. import db


class Citizen(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    # Additional fields

    def __repr__(self):
        return 'Citizen {}>'.format(self.id)
