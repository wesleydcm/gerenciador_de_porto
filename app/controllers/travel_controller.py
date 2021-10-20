from http import HTTPStatus

from app.models.travel_model import Travel
from flask import current_app, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.orm import exc

from .utils import session


@jwt_required()
def get_by_travel_code(travel_code: str):
    try:
        requester_username = get_jwt_identity()['username']

        travel: Travel = Travel.query.filter_by(travel_code=travel_code).first()

        if not travel:
            return {'msg': 'travel not found'}, HTTPStatus.NOT_FOUND

        travel.check_authorization(requester_username)

        return jsonify(travel), HTTPStatus.OK
    
    except PermissionError as e:
        return jsonify({'msg': str(e)}), HTTPStatus.BAD_REQUEST


@jwt_required()
def register_travel():
    requester_username = get_jwt_identity()['username']
    data = request.json

    new_travel = Travel(**data)
    new_travel.check_authorization(requester_username)
    new_travel.generate_travel_code()

    session(new_travel, "add")

    return jsonify(new_travel), HTTPStatus.CREATED


@jwt_required()
def update_travel(travel_code: str):
    try:
        requester_username = get_jwt_identity()['username']

        travel: Travel = Travel.query.filter_by(travel_code = travel_code).first()

        if not travel:
            return {'msg': 'travel not found'}, HTTPStatus.NOT_FOUND

        travel.check_authorization(requester_username)

        data = request.json


        if data:
            for key, value in data.items():
                setattr(travel, key, value)

            Travel.query.filter_by(travel_code=travel_code).update(data)
            current_app.db.session.commit()

        return jsonify(travel), HTTPStatus.OK
    
    except PermissionError as e:
        return jsonify({'msg': str(e)}), HTTPStatus.BAD_REQUEST


@jwt_required()
def delete_travel(travel_code: str):

    try:
        travel = Travel.query.filter_by(travel_code=travel_code).first()

        session(travel, "remove")

        return jsonify(travel), HTTPStatus.OK

    except exc.UnmappedInstanceError:
        return {'msg': 'travel not found, please review travel_code'}, HTTPStatus.BAD_REQUEST


@jwt_required()
def get_all_containers_in_travel(travel_code: str):

    travel = Travel.query.filter_by(travel_code=travel_code).first()

    if not travel:
        return {'msg': 'travel not found'}, HTTPStatus.NOT_FOUND

    return jsonify(travel.containers), HTTPStatus.OK
