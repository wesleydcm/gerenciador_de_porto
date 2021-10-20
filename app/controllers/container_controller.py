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


def check_owner(user_from_jwt, tracking):
    user = User.query.filter_by(username=user_from_jwt['username']).first()

    container = Container.query.filter_by(tracking_code=tracking).first()

    if not container:
        return {'msg': 'Container not found'}, HTTPStatus.NOT_FOUND

    shipping_company = ShippingCompany.query\
        .filter_by(id_user=user.id_user).first()

    if shipping_company.id_shipping_company != container.id_shipping_company:
        return {
            'msg': f'This tracking code {tracking} does not belong to your company'
        }, HTTPStatus.BAD_REQUEST


@jwt_required()
def create_container():
    try:
        current_tracking_code = generate_random_alphanumeric(5)
        user_from_jwt = get_jwt_identity()
        user = User.query.filter_by(username=user_from_jwt['username']).first()

        data = request.json

        shipping_company = ShippingCompany.query\
            .filter_by(trading_name=data["company"]).first()

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
        print(new_container)
        session(new_container, "add")

        return jsonify(new_container), HTTPStatus.CREATED

    except sqlalchemy.exc.IntegrityError as e:
        if type(e.orig) == NotNullViolation:
            return {'msg': 'Tracking code is required'}, HTTPStatus.BAD_REQUEST
        if type(e.orig) == UniqueViolation:
            return {'msg': 'Tracking code already registered'},
            HTTPStatus.BAD_REQUEST

    except CompanyNotPermission:
        return {
            "Error": "This company does not belong you!"
        }, HTTPStatus.BAD_REQUEST


@jwt_required()
def get_container_by_tracking_code(tracking_code: int):
    user_from_jwt = get_jwt_identity()

    container = Container.query.filter_by(tracking_code=tracking_code).first()

    check = check_owner(user_from_jwt, tracking_code)

    if check:
        return check

    return jsonify(container), HTTPStatus.OK


@jwt_required()
def update_container_by_tracking_code(tracking_code: int):
    user_from_jwt = get_jwt_identity()
    data = request.json

    if "tracking_code" in data:
        return {"Error": "It is not allowed to change the tracking_code"}

    check = check_owner(user_from_jwt, tracking_code)

    if check:
        return check

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
    check = check_owner(user_from_jwt, tracking_code)

    if check:
        return check

    container = Container.query.filter_by(tracking_code=tracking_code).first()

    session(container, "remove")

    return {}, HTTPStatus.NO_CONTENT


@jwt_required()
def get_travels_of_container(tracking_code: int):
    user_from_jwt = get_jwt_identity()
    check = check_owner(user_from_jwt, tracking_code)

    if check:
        return check

    container = Container.query.filter_by(tracking_code=tracking_code).first()

    return jsonify(container.travels), HTTPStatus.OK


@jwt_required()
def get_every_harbor_container_has_been(tracking_code: int):
    user_from_jwt = get_jwt_identity()
    check = check_owner(user_from_jwt, tracking_code)

    if check:
        return check

    container = Container.query.filter_by(tracking_code=tracking_code).first()

    return jsonify(container.harbors), HTTPStatus.OK


@jwt_required()
def container_locate(tracking_code: str):
    user_from_jwt = get_jwt_identity()
    check = check_owner(user_from_jwt, tracking_code)

    if check:
        return check

    container = Container.query.filter_by(tracking_code=tracking_code).first()

    container_harbor_item = ContainerHarbor.query.filter(ContainerHarbor.id_container == container.id_container)\
            .order_by(ContainerHarbor.id_container_harbor.desc()).first()
        
    if container_harbor_item and container_harbor_item.exit_date == None:
        return {'msg': f'Container {container.tracking_code} is on harbor {container.harbors.name}.'}, HTTPStatus.OK
    else:
        return {'msg': f'Container {container.tracking_code} is with his owner.'}, HTTPStatus.OK

    