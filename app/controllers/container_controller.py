from dataclasses import asdict

from app.models.container_model import Container
from flask import current_app, jsonify, request


def get_one_container(id:int):

    container = Container.query.get(id)

    if not container:
        return {'msg': 'container not found'}, 404
    
    return jsonify(container), 200
