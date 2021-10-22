from http import HTTPStatus
import sqlalchemy
from app.exceptions.containers_errors import CompanyNotPermission
from app.models.company_model import ShippingCompany
from app.models.container_model import Container
from app.models.container_harbor_model import ContainerHarbor
from app.models.user_model import User
from flask import jsonify, request
from flask_jwt_extended.utils import get_jwt_identity
from flask_jwt_extended.view_decorators import jwt_required
from psycopg2.errors import NotNullViolation, UniqueViolation
from app.controllers.utils import session, generate_random_alphanumeric


@jwt_required()
def create_container():
    try:
        current_tracking_code = generate_random_alphanumeric(5)
        user_from_jwt = get_jwt_identity()
        user = User.query.filter_by(username=user_from_jwt['username']).first()

        data = request.json

        if data.get('teu'):
            if data['teu'] != 1 and data['teu'] != 2:
                return {'msg': 'Teu must be equal to 1 or 2.'}

        shipping_company = ShippingCompany.query\
            .filter_by(trading_name=data["company"])\
            .first()

        if user.id_user != shipping_company.id_user:
            raise CompanyNotPermission

        data['id_shipping_company'] = shipping_company.id_shipping_company

        all_containers = Container.query.all()

        tracking = [code.tracking_code for code in all_containers]
        while current_tracking_code in tracking:
            current_tracking_code = generate_random_alphanumeric(5)

        data["tracking_code"] = current_tracking_code
        del(data["company"])

        new_container = Container(**data)
        session(new_container, "add")

        return jsonify(new_container), HTTPStatus.CREATED

    except sqlalchemy.exc.IntegrityError as e:
        if type(e.orig) == NotNullViolation:
            return {'msg': 'Tracking code is required'}, HTTPStatus.BAD_REQUEST
        if type(e.orig) == UniqueViolation:
            return {'msg': 'Tracking code already registered'}, HTTPStatus.BAD_REQUEST

    except CompanyNotPermission:
        return {
            "Error": "This company does not belong you!"
        }, HTTPStatus.BAD_REQUEST


@jwt_required()
def get_container_by_tracking_code(tracking_code: int):
    try:
        user_from_jwt = get_jwt_identity()["username"]

        container = Container.query\
            .filter_by(tracking_code=tracking_code)\
            .first()

        user = User.query.filter_by(id_user=container.company.id_user).first()

        if user.username == user_from_jwt:
            return jsonify(container), HTTPStatus.OK
        else:
            raise TypeError

    except AttributeError:
        return {"Error": "Tracking code invalid!"}, HTTPStatus.BAD_REQUEST

    except TypeError:
        return {"Error": "This user does not allowed to handle containers!"}


@jwt_required()
def update_container_by_tracking_code(tracking_code: int):
    data = request.json

    if "tracking_code" in data:
        return {"Error": "It is not allowed to change the tracking_code"}

    user_from_jwt = get_jwt_identity()["username"]

    container = Container.query.filter_by(tracking_code=tracking_code).first()
    user = User.query.filter_by(id_user=container.company.id_user).first()

    if user.username == user_from_jwt:
        try:
            Container.query.filter_by(tracking_code=tracking_code).update(data)

            updated_container = Container.query\
                .filter_by(tracking_code=tracking_code)\
                .first()

            return jsonify(updated_container), HTTPStatus.OK

        except sqlalchemy.exc.InvalidRequestError:
            return {
                'msg': 'check the data to be updated'
            }, HTTPStatus.BAD_REQUEST


@jwt_required()
def delete_container_by_tracking_code(tracking_code: int):
    user_from_jwt = get_jwt_identity()["username"]

    container = Container.query.filter_by(tracking_code=tracking_code).first()
    user = User.query.filter_by(id_user=container.company.id_user).first()

    if user.username == user_from_jwt:
        session(container, "remove")
        return {}, HTTPStatus.NO_CONTENT



    try:
        user_from_jwt = get_jwt_identity()["username"]

        container = Container.query\
            .filter_by(tracking_code=tracking_code)\
            .first()
        user = User.query.filter_by(id_user=container.company.id_user).first()

        if user.username == user_from_jwt:
            return jsonify(container.harbors), HTTPStatus.OK
        else:
            raise TypeError

    except AttributeError:
        return {"Error": "Tracking code invalid!"}, HTTPStatus.BAD_REQUEST

    except TypeError:
        return {
            "Error": "This container does not belong to this company!"
        }, HTTPStatus.BAD_REQUEST


@jwt_required()
def get_all():
    try:
        user_from_jwt = get_jwt_identity()["username"]
        user = User.query.filter_by(username=user_from_jwt).first()

        data = request.json
        company = ShippingCompany.query\
            .filter_by(trading_name=data["company"])\
            .first()

        if user.id_user == company.id_user:
            containers = Container.query\
                .filter_by(id_shipping_company=company.id_shipping_company)\
                .all()
            return jsonify(containers), HTTPStatus.OK

    except AttributeError:
        return {"Error": "Company does not exists!"}, HTTPStatus.BAD_REQUEST
