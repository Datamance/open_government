from .. import ma
from ..models.citizen import Citizen


class CitizenSchema(ma.ModelSchema):

    class Meta:
        model = Citizen


citizen_schema = CitizenSchema()
citizens_schema = CitizenSchema(many=True)
