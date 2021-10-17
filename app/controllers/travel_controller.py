from dataclasses import asdict
from http import HTTPStatus

from app.models.travel_model import Travel
from flask import current_app, jsonify, request

from .utils import generate_random_alphanumeric, session
from sqlalchemy.orm import exc

def get_by_travel_code(travel_code: str):

    travel = Travel.query.filter_by(travel_code = travel_code).first()

    if not travel:
        return {'msg': 'travel not found'}, HTTPStatus.NOT_FOUND
    
    return jsonify(travel), HTTPStatus.OK


def register_travel():
    data = request.json
    new_travel = Travel(**data)
    new_travel.generate_travel_code()
    session(new_travel, "add")

    return jsonify(new_travel), HTTPStatus.CREATED


def update_travel(travel_code: str):
    travel = Travel.query.filter_by(travel_code = travel_code).first()

    if not travel:
        return {'msg': 'travel not found'}, HTTPStatus.NOT_FOUND

    data = request.json

    if data:
        for key, value in data.items():
            setattr(travel, key, value)

        Travel.query.filter_by(travel_code=travel_code).update(data)
        current_app.db.session.commit()

    return jsonify(travel), HTTPStatus.OK


def delete_travel(travel_code: str):
    try:
        travel = Travel.query.filter_by(travel_code=travel_code).first()

        session(travel, "remove")

        return jsonify(travel), HTTPStatus.OK

    except exc.UnmappedInstanceError:
        return {'msg': 'travel not found, please review travel_code'}, HTTPStatus.BAD_REQUEST