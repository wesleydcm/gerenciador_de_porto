from dataclasses import asdict

from app.models.harbor_model import Harbor
from flask import current_app, jsonify, request


def get_one_harbor(id:int):

    harbor = Harbor.query.get(id)

    if not harbor:
        return {'msg': 'harbor not found'}, 404
    
    return jsonify(harbor), 200
