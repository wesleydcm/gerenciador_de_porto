from dataclasses import asdict
from http import HTTPStatus

from app.models.user_model import User
from flask import current_app, jsonify, request


def register_user():
    data = request.json

    new_user = User(**data)

    return jsonify(new_user), HTTPStatus.CREATED



def get_one_user(id:int):

    user = User.query.get(id)

    if not user:
        return {'msg': 'user not found'}, 404
    
    return jsonify(user), 200
