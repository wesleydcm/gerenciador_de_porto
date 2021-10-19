from dataclasses import asdict
from http import HTTPStatus

from app.models.container_model import Container
from flask import current_app, jsonify, request


def list_containers():
    containers = Container.query.all()

    return jsonify(containers), HTTPStatus.OK


def get_one_container(id_container:int):

    container = Container.query.get(id_container)

    if not container:
        return {'msg': 'container not found'}, 404
    
    return jsonify(container), 200
