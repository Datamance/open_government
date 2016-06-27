from ..webapp import database as db
from .mixins import Document


class Proposal(Document, db.Model):
    """
    Proposals.

    TODO(rico): Flesh out the proposal framework.
    """
    pass
