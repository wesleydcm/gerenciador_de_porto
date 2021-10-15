from flask import request, jsonify, current_app
from app.models.navio_model import NavioModel
from dataclasses import asdict


def get_one_ship(id:int):

    ship = NavioModel.query.get(id)
    
    return jsonify(ship), 200

    