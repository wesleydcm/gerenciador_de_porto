from dataclasses import asdict

from app.models.travel_model import Travel
from app.models.company_model import ShippingCompany
from app.models.ship_model import Ship
from app.models.user_model import User
from app.models.container_travel_model import ContainerTravel
from flask import current_app, jsonify, request

def get_one_travel(id:int):

    travel = Travel.query.get(id)

    if not travel:
        return {'msg': 'travel not found'}, 404
    
    return jsonify(travel), 200
