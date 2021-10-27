from sqlalchemy.exc import IntegrityError, InvalidRequestError
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify, request, current_app
from http import HTTPStatus

from app.models.company_model import ShippingCompany
from app.models.ship_harbor_model import ShipHarbor
from app.controllers.utils import session
from app.models.ship_model import Ship
from app.models.user_model import User


@jwt_required()
def create_ship():
    try:
        user_from_jwt = get_jwt_identity()
        user = User.query.filter_by(username=user_from_jwt['username']).first()

        data = request.json
        companyName = data.pop("company")
        company = ShippingCompany.query.filter_by(
            trading_name=companyName
            ).first()
        if not company:
            return {"Error": "Company not found."}, HTTPStatus.NOT_FOUND

        if company.id_user != user.id_user:
            return {
                "Error": "User does not have credentials of this company"
                }, HTTPStatus.UNAUTHORIZED

        data["id_shipping_company"] = company.id_shipping_company

        new_ship = Ship(**data)
        session(new_ship, "add")
        return jsonify(new_ship), HTTPStatus.CREATED

    except IntegrityError:
        return {"Error": "Ship already registered."}, HTTPStatus.CONFLICT

    except TypeError as err:
        return {"Error": str(err)}, HTTPStatus.BAD_REQUEST


@jwt_required()
def info_ship(name_ship: str):
    try:
        data_user = get_jwt_identity()["username"]
        ship = Ship.query\
            .filter_by(name=name_ship)\
            .first()

        if not ship:
            return {'Error': 'Ship not found.'}, HTTPStatus.NOT_FOUND

        user = User.query.filter_by(id_user=ship.company.id_user).first()

        if user.username == data_user:
            return jsonify(ship), HTTPStatus.OK

    except TypeError:
        return{
            "Error": "This ship does not belong to your company!"
        }, HTTPStatus.BAD_REQUEST


@jwt_required()
def update_ship(name_ship: str):
    try:
        data = request.json
        data_user = get_jwt_identity()["username"]
        ship = Ship.query\
            .filter_by(name=name_ship)\
            .first()

        if not ship:
            return {'Error': 'Ship not found.'}, HTTPStatus.NOT_FOUND

        user = User.query.filter_by(id_user=ship.company.id_user).first()

        if user.username == data_user:
            Ship.query.filter_by(name=name_ship).update(data)
            current_app.db.session.commit()
            return jsonify(ship), HTTPStatus.OK

    except InvalidRequestError as err:
        return {
            "Error": "Field " + str(err).split('"')[-2] + " does not exists."
        }, HTTPStatus.BAD_REQUEST


@jwt_required()
def delete_ship(name_ship: str):
    data_user = get_jwt_identity()["username"]
    ship = Ship.query\
        .filter_by(name=name_ship)\
        .first()

    if not ship:
        return {'Error': 'Ship not found.'}, HTTPStatus.NOT_FOUND

    user = User.query.filter_by(id_user=ship.company.id_user).first()

    if user.username == data_user:
        session(ship, "remove")
        return {}, HTTPStatus.NO_CONTENT


@jwt_required()
def all_ship_travel(name_ship: str):
    data_user = get_jwt_identity()["username"]
    ship = Ship.query\
        .filter_by(name=name_ship)\
        .first()

    if not ship:
        return {'Error': 'Ship not found.'}, HTTPStatus.NOT_FOUND

    user = User.query.filter_by(id_user=ship.company.id_user).first()

    if user.username == data_user:
        if len(ship.travel) < 1:
            return {"Error": "No trip recorded."}, HTTPStatus.NOT_FOUND

        return jsonify(ship.travel), HTTPStatus.OK


@jwt_required()
def ship_locate(name_ship: str):
    data_user = get_jwt_identity()["username"]
    ship = Ship.query\
        .filter_by(name=name_ship)\
        .first()

    if not ship:
        return {'msg': 'Ship not found.'}, HTTPStatus.NOT_FOUND

    user = User.query.filter_by(id_user=ship.company.id_user).first()

    if user.username == data_user:
        ship_harbor_item = ShipHarbor.query\
            .filter(ShipHarbor.id_ship == ship.id_ship)\
            .order_by(ShipHarbor.id_ship_harbor.desc())\
            .first()

        if ship_harbor_item and ship_harbor_item.exit_date == None:
            return {
                'msg': f'{ship.name} is on harbor {ship_harbor_item.harbor.name}.'
            }, HTTPStatus.OK
        else:
            return {'msg': f'{ship.name} is with his owner.'}, HTTPStatus.OK
