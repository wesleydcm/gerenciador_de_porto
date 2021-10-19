from dataclasses import asdict

from app.models.ship_model import Ship
from flask import current_app, jsonify, request


def get_one_ship(id:int):

    ship = Ship.query.get(id)

    if not ship:
        return {'msg': 'ship not found'}, 404

    return jsonify(ship), 200
