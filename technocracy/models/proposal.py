from ..webapp import database as db


class Proposal(db.Model):
    """
    Proposals.

    TODO(rico): Flesh out the proposal framework.
    """

    __tablename__ = 'proposals'

    id = db.Column(db.Integer, primary_key=True)
    # Additional fields

    def __repr__(self):
        return 'Proposal {}>'.format(self.id)
