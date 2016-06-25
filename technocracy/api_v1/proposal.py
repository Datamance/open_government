from flask import jsonify, request

from . import api
from .. import db
from ..models.proposal import Proposal
from ..schemas.proposal import proposal_schema, proposals_schema


@api.route('/proposals', methods=['GET'])
def get_proposals():
    pass


@api.route('/proposals/<int:id>', methods=['GET'])
def get_proposal(id):
    pass


@api.route('/proposals', methods=['POST'])
def create_proposal():
    pass


@api.route('/proposals/<int:id>', methods=['PUT'])
def update_proposal(id):
    pass


@api.route('/proposals/<int:id>', methods=['DELETE'])
def delete_proposal(id):
    pass
