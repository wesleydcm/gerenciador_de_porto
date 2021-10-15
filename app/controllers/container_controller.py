from flask import request, jsonify, current_app
from app.models.container_model import ContainerModel
from dataclasses import asdict


def get_one_container(id:int):

    container = ContainerModel.query.get(id)
    
    return jsonify(container), 200

