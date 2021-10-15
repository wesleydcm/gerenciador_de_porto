from flask import request, jsonify, current_app
from app.models.container_model import ContainerModel
from dataclasses import asdict


def get_one_container(id:int):

    container = ContainerModel.query.get(id)

    if not container:
        return {'msg': 'container not found'}, 404
    
    return jsonify(container), 200

