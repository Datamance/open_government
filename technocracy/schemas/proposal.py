from .. import ma
from ..models.proposal import Proposal


class ProposalSchema(ma.ModelSchema):

    class Meta:
        model = Proposal


proposal_schema = ProposalSchema()
proposals_schema = ProposalSchema(many=True)
