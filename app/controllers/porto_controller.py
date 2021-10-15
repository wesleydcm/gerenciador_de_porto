from flask import request, jsonify, current_app
from app.models.porto_model import PortoModel
from dataclasses import asdict


def get_one_harbor(id:int):

    harbor = PortoModel.query.get(id)
    
    return jsonify(harbor), 200

    