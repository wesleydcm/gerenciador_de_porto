from dataclasses import asdict

from app.models.travel_model import Travel
from flask import current_app, jsonify, request


def get_one_travel(id:int):

    travel = Travel.query.get(id)

    if not travel:
        return {'msg': 'travel not found'}, 404
    
    return jsonify(travel), 200
