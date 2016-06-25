from flask import jsonify, request

from . import api
from .. import db
from ..models.citizen import Citizen
from ..schemas.citizen import citizen_schema, citizens_schema


@api.route('/citizens', methods=['GET'])
def get_citizens():
    pass


@api.route('/citizens/<int:id>', methods=['GET'])
def get_citizen(id):
    pass


@api.route('/citizens', methods=['POST'])
def create_citizen():
    pass


@api.route('/citizens/<int:id>', methods=['PUT'])
def update_citizen(id):
    pass


@api.route('/citizens/<int:id>', methods=['DELETE'])
def delete_citizen(id):
    pass
