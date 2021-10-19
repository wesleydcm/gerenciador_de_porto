from http import HTTPStatus

from app.controllers.utils import session
from app.models.ship_model import Ship
from flask import jsonify, request
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError, InvalidRequestError


@jwt_required()
def create_ship():
    try:
        data = request.json
        new_ship = Ship(**data)
        session(new_ship, "add")
        return jsonify(new_ship), HTTPStatus.CREATED

    except IntegrityError:
        return {"msg": "Ship already registered."}, HTTPStatus.CONFLICT

    except TypeError as err:
        return {"msg": str(err)}, HTTPStatus.BAD_REQUEST


@jwt_required()
def info_ship(name_ship: str):
    ship = Ship.query.filter_by(name=name_ship).first()
    if not ship:
        return {'msg': 'Ship not found.'}, HTTPStatus.NOT_FOUND

    return jsonify(ship), HTTPStatus.OK


@jwt_required()
def update_ship(name_ship: str):
    data = request.json
    try:
        ship = Ship.query.filter_by(name=name_ship).first()
        if not ship:
            return {'msg': 'Ship not found.'}, HTTPStatus.NOT_FOUND

        Ship.query.filter_by(name=name_ship).update(data)
        session(ship, "add")
        return jsonify(ship), HTTPStatus.OK

    except InvalidRequestError as err:
        return {
            "msg": "Field " + str(err).split('"')[-2] + " does not exists."
            }, HTTPStatus.BAD_REQUEST


@jwt_required()
def delete_ship(name_ship: str):
    ship = Ship.query.filter_by(name=name_ship).first()
    if not ship:
        return {'msg': 'Ship not found.'}, HTTPStatus.NOT_FOUND

    session(ship, "remove")
    return {}, HTTPStatus.OK


@jwt_required()
def all_ship_travel(name_ship: str):
    ship = Ship.query.filter_by(name=name_ship).first()
    if not ship:
        return {'msg': 'Ship not found.'}, HTTPStatus.NOT_FOUND

    if len(ship.travel) < 1:
        return {"msg": "No trip recorded."}, HTTPStatus.NOT_FOUND

    return jsonify(ship.travel), HTTPStatus.OK

