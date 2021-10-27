from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify, request, current_app
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from http import HTTPStatus

from app.exceptions.company_erros import UserIsHarbor
from app.models.company_model import ShippingCompany
from app.controllers.user_controller import session
from app.models.user_model import User


@jwt_required()
def register_company():
    try:
        data = request.get_json()
        data["created_at"] = datetime.utcnow()

        user_data = get_jwt_identity()
        user = User.query.filter_by(username=user_data["username"]).first()

        if user.is_harbor:
            raise UserIsHarbor

        data["id_user"] = user.id_user

        new_company = ShippingCompany(**data)
        session(new_company, "add")

        return {"msg": "Shipping Company created!"}, HTTPStatus.CREATED

    except UserIsHarbor:
        return {
            "Error": "This user cannot create a company"
        }, HTTPStatus.BAD_REQUEST

    except IntegrityError as err:
        return str(err).split('\n')[1], HTTPStatus.CONFLICT


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


@jwt_required()
def list_containers_by_company(trading_name: str):
    try:
        user_data = get_jwt_identity()
        user = User.query.filter_by(username=user_data["username"]).first()

        for company in user.company:
            if company.trading_name == trading_name:
                current_company = company

        return jsonify(current_company.containers), HTTPStatus.OK

    except UnboundLocalError:
        return {"Error": "Company not found!"}, HTTPStatus.BAD_REQUEST


@jwt_required()
def list_ships_by_company(trading_name: str):
    try:
        user_data = get_jwt_identity()
        user = User.query.filter_by(username=user_data["username"]).first()

        for company in user.company:
            if company.trading_name == trading_name:
                current_company = company

        return jsonify(current_company.ships), HTTPStatus.OK

    except UnboundLocalError:
        return {"Error": "Company not found!"}, HTTPStatus.BAD_REQUEST
