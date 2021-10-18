from app.models.ship_model import Ship
from flask import current_app, jsonify, request
# from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError, InvalidRequestError


# @jwt_required()
def create_ship():
    try:
        data = request.json
        new_ship = Ship(**data)

        current_app.db.session.add(new_ship)
        current_app.db.session.commit()

        return jsonify(new_ship), 201

    except IntegrityError:
        return {"msg": "Ship already registered."}, 409

    except TypeError as err:
        return {"msg": str(err)}, 400


# @jwt_required()
def info_ship(name_ship: str):
    ship = Ship.query.filter_by(name=name_ship).first()
    if not ship:
        return {'msg': 'Ship not found.'}, 404

    return jsonify(ship), 200


# @jwt_required()
def update_ship(name_ship: str):
    data = request.json
    try:
        ship = Ship.query.filter_by(name=name_ship).first()
        if not ship:
            return {'msg': 'Ship not found.'}, 404

        Ship.query.filter_by(name=name_ship).update(data)

        current_app.db.session.add(ship)
        current_app.db.session.commit()

        return jsonify(ship), 200

    except InvalidRequestError as err:
        return {
            "msg": "Field " + str(err).split('"')[-2] + " does not exists."
            }, 400


# @jwt_required()
def delete_ship(name_ship: str):
    ship = Ship.query.filter_by(name=name_ship).first()
    if not ship:
        return {'msg': 'Ship not found.'}, 404

    current_app.db.session.delete(ship)
    return {}, 204


# @jwt_required()
def all_ship_travel(name_ship: str):
    ship = Ship.query.filter_by(name=name_ship).first()
    if not ship:
        return {'msg': 'Ship not found.'}, 404

    if len(ship.travel) < 1:
        return {"msg": "No trip recorded."}, 404

    return jsonify(ship.travel), 200
