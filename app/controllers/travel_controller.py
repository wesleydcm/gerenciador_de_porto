from http import HTTPStatus
from app.models.container_model import Container
from app.models.travel_model import Travel
from app.models.company_model import ShippingCompany
from app.models.ship_model import Ship
from app.models.user_model import User
from app.models.container_travel_model import ContainerTravel
from flask import current_app, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm import exc
from app.controllers.utils import generate_random_alphanumeric
from datetime import datetime
from .utils import session


@jwt_required()
def get_by_travel_code(travel_code: str):
    try:
        travel = Travel.query.filter_by(travel_code=travel_code).first()
        if not travel:
            return {
                "Error": "Travel not found, please review 'travel_code'."
            }, HTTPStatus.NOT_FOUND

        requester_username = get_jwt_identity()['username']
        user = User.query.filter_by(username=requester_username).first()

        company_id = travel.ship.id_shipping_company
        company = ShippingCompany.query\
            .filter_by(id_shipping_company=company_id)\
            .first()

        if company.id_user == user.id_user:
            return jsonify(travel), HTTPStatus.OK

    except PermissionError as e:
        return jsonify({'msg': str(e)}), HTTPStatus.BAD_REQUEST

    except TypeError:
        return {
            "Error": "Travel not found, please review 'travel_code'."
        }, HTTPStatus.BAD_REQUEST


@jwt_required()
def register_travel():
    try:
        data = request.json
        current_travel_code = generate_random_alphanumeric(6)

        requester_username = get_jwt_identity()['username']
        user = User.query.filter_by(username=requester_username).first()

        company_name = data.pop("company")
        company = ShippingCompany.query\
            .filter_by(trading_name=company_name)\
            .first()

        ship_name = data.pop("name_ship")
        ship = Ship.query.filter_by(name=ship_name).first()
        data["id_ship"] = ship.id_ship

        all_travels = Travel.query.all()

        travel_code = [travel.travel_code for travel in all_travels]
        while current_travel_code in travel_code:
            current_travel_code = generate_random_alphanumeric(6)

        data["travel_code"] = current_travel_code

        if company.id_shipping_company == ship.id_shipping_company and company.id_user == user.id_user:
            new_travel = Travel(**data)
            session(new_travel, "add")
            return jsonify(new_travel), HTTPStatus.CREATED

    except AttributeError:
        return {
            "Error": "You are not allowed to handle data of this company!"
        }, HTTPStatus.UNAUTHORIZED


@jwt_required()
def update_travel(travel_code: str):
    try:
        travel = Travel.query.filter_by(travel_code=travel_code).first()

        if not travel:
            return {
                'Error': "Travel not found, please review 'travel_code'."
            }, HTTPStatus.NOT_FOUND

        requester_username = get_jwt_identity()['username']
        user = User.query.filter_by(username=requester_username).first()

        data = request.json
        company_id = travel.ship.id_shipping_company
        company = ShippingCompany.query\
            .filter_by(id_shipping_company=company_id)\
            .first()

        if company.id_user == user.id_user:
            Travel.query.filter_by(travel_code=travel_code).update(data)
            current_app.db.session.commit()

        return jsonify(travel), HTTPStatus.OK
    except exc.UnmappedInstanceError:
        return {
            "Error": "Travel not found, please review 'travel_code'."
        }, HTTPStatus.BAD_REQUEST

    except PermissionError as e:
        return jsonify({'msg': str(e)}), HTTPStatus.BAD_REQUEST


@jwt_required()
def delete_travel(travel_code: str):
    try:
        travel = Travel.query.filter_by(travel_code=travel_code).first()

        if not travel:
            return {
                'Error': "Travel not found, please review 'travel_code'."
            }, HTTPStatus.NOT_FOUND

        requester_username = get_jwt_identity()['username']
        user = User.query.filter_by(username=requester_username).first()

        company_id = travel.ship.id_shipping_company
        company = ShippingCompany.query\
            .filter_by(id_shipping_company=company_id)\
            .first()

        if company.id_user == user.id_user:
            session(travel, "remove")
            return {}, HTTPStatus.NO_CONTENT

    except exc.UnmappedInstanceError:
        return {
            "Error": "Travel not found, please review 'travel_code'."
        }, HTTPStatus.BAD_REQUEST

    except PermissionError as e:
        return jsonify({'msg': str(e)}), HTTPStatus.BAD_REQUEST


@jwt_required()
def add_container_in_travel(travel_code: str):
    requester_username = get_jwt_identity()['username']
    data = request.json
    try:
        travel = Travel.query.filter_by(travel_code=travel_code).first()
        if not travel:
            return {
                'Error': f'No Travel found with the travel_code: {travel_code}'
            }, HTTPStatus.NOT_FOUND

        ship = Ship.query.filter_by(id_ship=travel.id_ship).first()
        company = ShippingCompany.query.filter_by(id_shipping_company=ship.id_shipping_company).first()
        user = User.query.filter_by(username=requester_username).first()
        container = Container.query.filter_by(tracking_code=data["tracking_code"]).first()
        container_travel = ContainerTravel.query.filter_by(id_container=container.id_container).first()

        if user.id_user != company.id_user:
            return{
                'Error': 'This travel does not belong to you'
            }, HTTPStatus.BAD_REQUEST

        if not container:
            return {
                'Error': f'Tracking code({data["tracking_code"]}) of container not found'
            }, HTTPStatus.BAD_REQUEST

        if not container_travel:
            container_travel = ContainerTravel(
            created_at=datetime.utcnow(),
            last_update=datetime.utcnow(),
            id_container=container.id_container,
            id_travel=travel.id_travel
        )
            session(container_travel, "add")
            return jsonify(container), HTTPStatus.CREATED
        
        elif container_travel and container_travel.last_update == container_travel.created_at:
            container_travel.last_update = datetime.utcnow()
            
            current_app.db.session.commit()
            return jsonify(container), HTTPStatus.CREATED

        elif container_travel and container_travel.last_update != container_travel.created_at:
            return {
                'msg': f'Container {container.tracking_code} already added to this travel.'
            }, HTTPStatus.CONFLICT
 
    except PermissionError as e:
        return jsonify({'msg': str(e)}), HTTPStatus.BAD_REQUEST


@jwt_required()
def get_all_containers_in_travel(travel_code: str):

    try:
        travel = Travel.query.filter_by(travel_code=travel_code).first()

        requester_username = get_jwt_identity()['username']
        user = User.query.filter_by(username=requester_username).first()

        company_id = travel.ship.id_shipping_company
        company = ShippingCompany.query\
            .filter_by(id_shipping_company=company_id)\
            .first()

        if company.id_user == user.id_user:
            return jsonify(travel.containers), HTTPStatus.OK

    except (exc.UnmappedInstanceError, AttributeError):
        return {
            'Error': "Travel not found, please review 'travel_code'."
        }, HTTPStatus.BAD_REQUEST

    except PermissionError as e:
        return jsonify({'msg': str(e)}), HTTPStatus.BAD_REQUEST
