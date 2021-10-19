from http import HTTPStatus

import sqlalchemy
from app.models.company_model import ShippingCompany
from app.models.container_model import Container
from app.models.user_model import User
from flask import current_app, jsonify, request
from flask_jwt_extended.utils import get_jwt_identity
from flask_jwt_extended.view_decorators import jwt_required
from psycopg2.errors import NotNullViolation, UniqueViolation


def check_owner(user_from_jwt, tracking):
    user = User.query.filter_by(username=user_from_jwt['username']).first()

    container = Container.query.filter_by(tracking_code=tracking).first()

    if not container:
        return {'msg': 'Container not found'}, HTTPStatus.NOT_FOUND

    shipping_company = ShippingCompany.query\
        .filter_by(id_user=user.id_user).first()

    if shipping_company.id_shipping_company != container.id_shipping_company:
        return {'msg': f'This tracking code {tracking} does not belong to \
            your company'}, HTTPStatus.BAD_REQUEST


def list_containers():
    containers = Container.query.all()

    return jsonify(containers), HTTPStatus.OK


def get_one_container(id_container: int):

    container = Container.query.get(id_container)

    if not container:
        return {'msg': 'container not found'}, 404

    return jsonify(container), 200


@jwt_required()
def create_container():
    user_from_jwt = get_jwt_identity()
    user = User.query.filter_by(username=user_from_jwt['username']).first()

    data = request.json

    shipping_company = ShippingCompany.query\
        .filter_by(id_user=user.id_user).first()

    data['id_shipping_company'] = shipping_company.id_shipping_company

    try:
        new_container = Container(**data)

        current_app.db.session.add(new_container)
        current_app.db.session.commit()

        return jsonify(new_container), HTTPStatus.CREATED

    except sqlalchemy.exc.IntegrityError as e:
        if type(e.orig) == NotNullViolation:
            return {'msg': 'Tracking code is required'}, HTTPStatus.BAD_REQUEST
        if type(e.orig) == UniqueViolation:
            return {'msg': 'Tracking code already registered'},
            HTTPStatus.BAD_REQUEST


@jwt_required()
def get_container_by_tracking_code(tracking_code: int):
    user_from_jwt = get_jwt_identity()

    container = Container.query.filter_by(tracking_code=tracking_code).first()

    check_owner(user_from_jwt, tracking_code)

    return jsonify(container), HTTPStatus.OK


@jwt_required()
def update_container_by_tracking_code(tracking_code: int):
    user_from_jwt = get_jwt_identity()

    data = request.json

    check_owner(user_from_jwt, tracking_code)

    try:
        Container.query.filter_by(tracking_code=tracking_code).update(data)

        updated_container = Container.query\
            .filter_by(tracking_code=tracking_code)\
            .first()

        return jsonify(updated_container), HTTPStatus.OK

    except sqlalchemy.exc.InvalidRequestError:
        return {'msg': 'check the data to be updated'}, HTTPStatus.BAD_REQUEST


@jwt_required()
def delete_container_by_tracking_code(tracking_code: int):
    user_from_jwt = get_jwt_identity()

    check_owner(user_from_jwt, tracking_code)

    container = Container.query.filter_by(tracking_code=tracking_code).first()

    current_app.db.session.delete(container)
    current_app.db.session.commit()

    return {}, HTTPStatus.NO_CONTENT


@jwt_required()
def get_travels_of_container(tracking_code: int):
    user_from_jwt = get_jwt_identity()

    check_owner(user_from_jwt, tracking_code)

    container = Container.query.filter_by(tracking_code=tracking_code).first()

    return jsonify(container.travels), HTTPStatus.OK


@jwt_required()
def get_every_harbor_container_has_been(tracking_code: int):
    user_from_jwt = get_jwt_identity()

    check_owner(user_from_jwt, tracking_code)

    container = Container.query.filter_by(tracking_code=tracking_code).first()

    return jsonify(container.harbors), HTTPStatus.OK
