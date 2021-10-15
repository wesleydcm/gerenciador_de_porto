from flask import request, jsonify, current_app
from app.models.viagem_model import ViagemModel
from dataclasses import asdict


def get_one_travel(id:int):

    travel = ViagemModel.query.get(id)
    
    return jsonify(travel), 200

    