from flask import jsonify, request, current_app
from http import HTTPStatus
from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.company_model import ShippingCompany
from app.models.container_model import Container
from app.controllers.user_controller import session
from app.models.company_model import ShippingCompany
from app.models.user_model import User


@jwt_required()
def register_company():
    data = request.get_json()
    data["created_at"] = datetime.now().strftime("%d/%m/%Y")

    user_data = get_jwt_identity()
    user = User.query.filter_by(username=user_data["username"]).first()
    data["id_user"] = user.id_user

    new_company = ShippingCompany(**data)
    session(new_company, "add")

    return jsonify(new_company), HTTPStatus.CREATED


@jwt_required()
def get_company(trading_name: str):
    try:
        user_data = get_jwt_identity()
        user = User.query.filter_by(username=user_data["username"]).first()

        for company in user.company:
            if company.trading_name == trading_name:
                current_company = company

        return jsonify(current_company), HTTPStatus.OK

    except UnboundLocalError:
        return {"Error": "Company not found!"}, HTTPStatus.BAD_REQUEST


@jwt_required()
def update(trading_name: str):
    try:
        data = request.get_json()

        user_data = get_jwt_identity()
        user = User.query.filter_by(username=user_data["username"]).first()

        for company in user.company:
            if company.trading_name == trading_name:
                current_company = company

        if current_company:
            ShippingCompany.query\
                .filter_by(trading_name=trading_name).update(data)
            current_app.db.session.commit()
            return jsonify(data), HTTPStatus.OK

    except UnboundLocalError:
        return {"Error": "Company not found!"}, HTTPStatus.BAD_REQUEST


@jwt_required()
def delete(trading_name: str):
    try:
        user_data = get_jwt_identity()
        user = User.query.filter_by(username=user_data["username"]).first()

        for company in user.company:
                if company.trading_name == trading_name:
                    current_company = company

        session(current_company, "remove")
        return {"trading_name": current_company.trading_name}, HTTPStatus.OK
    except UnboundLocalError:
        return {"Error": "Company not found!"}, HTTPStatus.BAD_REQUEST




def list_containers_by_company(id: int):

    company: ShippingCompany = ShippingCompany.query.get(id)

    containers = Container.query.filter_by(id_shipping_company = company.id_shipping_company).all()

    if not containers:
        return {'msg': "company does not have registered containers"}, HTTPStatus.NOT_FOUND

    return jsonify(containers), HTTPStatus.OK
