from datetime import datetime
from app.models.user_model import User
from app.models.harbor_model import Harbor
from app.models.ship_harbor_model import ShipHarbor
from app.models.ship_model import Ship
from app.models.container_harbor_model import ContainerHarbor
from app.models.container_model import Container
from app.models.container_travel_model import ContainerTravel
from app.models.travel_model import Travel
from app.controllers.utils import session
from flask import jsonify, request, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from http import HTTPStatus
import psycopg2
import sqlalchemy
from dataclasses import asdict


@jwt_required()
def create_harbor():
    current_username = get_jwt_identity()['username']
    user = User.query.filter_by(username=current_username).first()

    if user.is_harbor:
        try:
            data = request.json

            if data.get('teus') == None:
                return {
                    "Error": "null value in column \"teus\" of relation \"harbor\" violates not-null constraint"
                }, HTTPStatus.BAD_REQUEST

            if data.get('name') == None:
                return {
                    "Error": "null value in column \"name\" of relation \"harbor\" violates not-null constraint"
                }, HTTPStatus.BAD_REQUEST

            harbor_availability = data['teus']
            harbor_name = data['name'].capitalize()
            data['availability'] = harbor_availability
            data['name'] = harbor_name
            data['id_user'] = user.id_user

            harbor = Harbor(**data)
            session(harbor, 'add')

            return jsonify(harbor), HTTPStatus.CREATED

        except sqlalchemy.exc.IntegrityError as e:

            if type(e.orig) == psycopg2.errors.NotNullViolation:
                return {
                    'Error': str(e.orig).split('\n')[0]
                }, HTTPStatus.BAD_REQUEST

            return {'Error': str(e).split('\n')[1]}, HTTPStatus.CONFLICT

        except TypeError as e:
             return {'Error': str(e)}, HTTPStatus.BAD_REQUEST

    else:
        return {
            'Error': 'You are a company user. You are not allowed to handle harbors data.'
        }, HTTPStatus.UNAUTHORIZED


@jwt_required()
def get_one_harbor(harbor_name:str):
    current_username = get_jwt_identity()['username']
    user = User.query.filter_by(username=current_username).first()

    if user.is_harbor:
        try:
            harbor = Harbor.query.filter_by(name=harbor_name.capitalize()).one()
            return jsonify(harbor), HTTPStatus.OK

        except sqlalchemy.exc.NoResultFound:
            return {'Error': 'Harbor not found'}, HTTPStatus.NOT_FOUND
    else:
        return {'msg': 'You are a company user. You are not allowed to handle harbors data.'}, HTTPStatus.UNAUTHORIZED


@jwt_required()
def update_one_harbor(harbor_name:str):

    current_username = get_jwt_identity()['username']
    user = User.query.filter_by(username=current_username).first()

    data = request.json   

    if user.is_harbor:
        try:
            harbor = Harbor.query.filter_by(name=harbor_name.capitalize()).one()

            if data.get('teus'):
                container_harbor_list = ContainerHarbor.query.filter(ContainerHarbor.id_harbor == harbor.id_harbor,
                    ContainerHarbor.exit_date == None).all()

                occupied_teus = 0

                for container_harbor in container_harbor_list:
                    occupied_teus += container_harbor.container.teu

                harbor_availability = data['teus'] - occupied_teus
                data['availability'] = harbor_availability

            new_name = ''

            if data.get('name'):
                new_name = data['name'].capitalize()
                data['name'] = data['name'].capitalize()
            else:
                new_name  = harbor.name.capitalize()

            Harbor.query.filter_by(name=harbor_name.capitalize()).update(data)            
            current_app.db.session.commit()
            harbor = Harbor.query.filter_by(name=new_name).first()

            return jsonify(harbor), HTTPStatus.OK
            
        except sqlalchemy.exc.NoResultFound:
            return {'Error': 'Harbor not found'}, HTTPStatus.NOT_FOUND

        except sqlalchemy.exc.IntegrityError as e:
            return {'Error': str(e).split('\n')[1]}, HTTPStatus.CONFLICT

        except sqlalchemy.exc.InvalidRequestError as e:
            return {'Error': str(e)}, HTTPStatus.BAD_REQUEST    
    else:
        return {'msg': 'You are a company user. You are not allowed to handle harbors data.'}, HTTPStatus.UNAUTHORIZED


@jwt_required()
def get_containers_on_harbor_now(harbor_name:str):

    current_username = get_jwt_identity()['username']
    user = User.query.filter_by(username=current_username).first()

    if user.is_harbor:
        try:
            harbor = Harbor.query.filter_by(name=harbor_name.capitalize()).one()

            result_list = []                      

            for item in harbor.containers:
                item_dict = asdict(item)
                item_dict['dates_in_harbor'] = [{
                    'entry_date': item.entry_date, 
                    'exit_date': item.exit_date                      
                    } for item in item.container_harbor_dates if item.exit_date == None]
                
                if len(item_dict['dates_in_harbor']) > 0:
                    result_list.append(item_dict)

            return jsonify(result_list), HTTPStatus.OK

        except sqlalchemy.exc.NoResultFound:
            return {'Error': 'Harbor not found'}, HTTPStatus.NOT_FOUND
    else:
        return {'msg': 'You are a company user. You are not allowed to handle harbors data.'}, HTTPStatus.UNAUTHORIZED


@jwt_required()
def get_containers_on_harbor_all_times(harbor_name:str):

    current_username = get_jwt_identity()['username']
    user = User.query.filter_by(username=current_username).first()

    if user.is_harbor:
        try:
            harbor = Harbor.query.filter_by(name=harbor_name.capitalize()).one()

            result_list = []                      

            for item in harbor.containers:
                item_dict = asdict(item)
                item_dict['dates_in_harbor'] = [{
                    'entry_date': item.entry_date, 
                    'exit_date': item.exit_date                      
                    } for item in item.container_harbor_dates]
                result_list.append(item_dict)
                
            return jsonify(result_list), HTTPStatus.OK

        except sqlalchemy.exc.NoResultFound:
            return {'Error': 'Harbor not found'}, HTTPStatus.NOT_FOUND
    else:
        return {'msg': 'You are a company user. You are not allowed to handle harbors data.'}, HTTPStatus.UNAUTHORIZED


@jwt_required()
def update_containers_on_harbor(harbor_name: str):
    current_username = get_jwt_identity()['username']
    user = User.query.filter_by(username=current_username).first()
    
    data = request.json
    
    if user.is_harbor:
        harbor = Harbor.query.filter_by(name=harbor_name.capitalize()).first()
       
        container = Container.query.filter_by(tracking_code=data['tracking_code']).first()

        container_harbor_item = ContainerHarbor.query.filter(ContainerHarbor.id_container == container.id_container)\
            .order_by(ContainerHarbor.id_container_travel.desc()).first()     
                 
        if container_harbor_item and container_harbor_item.exit_date == None:
            container_harbor_item.exit_date = datetime.utcnow()
            harbor.availability += container.teu
            current_app.db.session.commit()
            container_harbor_item = ContainerHarbor.query.filter(
                ContainerHarbor.id_container == container.id_container
                )\
                .order_by(ContainerHarbor.id_container_travel.desc())\
                .first()
            new_item = {
                'container': container.tracking_code,
                'entry_date': container_harbor_item.entry_date,
                'exit_date': container_harbor_item.exit_date
            }
            return jsonify(new_item), HTTPStatus.CREATED
        
        elif not container_harbor_item or container_harbor_item.exit_date != None:
            current_time = datetime.utcnow()
            
            item = ContainerHarbor(entry_date=current_time)            
            item.container = container            
            harbor.container_harbor_items.append(item)            
            harbor.availability -= container.teu

            travel = Travel.query.filter_by(travel_code=data['travel_code']).first()
            container_travel_item = ContainerTravel.query.filter\
                (ContainerTravel.id_travel == travel.id_travel,\
                     ContainerTravel.id_container == container.id_container)\
                    .first()
            container_travel_item.last_update = current_time
            
            current_app.db.session.commit()
            
            container_harbor_item = ContainerHarbor.query.filter(
                ContainerHarbor.id_container == container.id_container
                )\
                .order_by(ContainerHarbor.id_container_travel.desc())\
                .first()
            new_item = {
                'container': container.tracking_code,
                'entry_date': container_harbor_item.entry_date
            }
            return jsonify(new_item), HTTPStatus.CREATED
    else:
        return {
            'msg': 'You are a company user. You are not allowed to handle harbors data.'
        }, HTTPStatus.UNAUTHORIZED


@jwt_required()
def get_ships_on_harbor_now(harbor_name:str):

    current_username = get_jwt_identity()['username']
    user = User.query.filter_by(username=current_username).first()

    if user.is_harbor:
        try:
            harbor = Harbor.query.filter_by(name=harbor_name.capitalize()).one()

            result_list = []
            
            for item in harbor.ships:
                item_dict = asdict(item)
                item_dict['dates_in_harbor'] = [{
                    'entry_date': item.entry_date, 
                    'exit_date': item.exit_date                      
                    } for item in item.ship_harbor_dates if item.exit_date == None]
                
                if len(item_dict['dates_in_harbor']) > 0:
                    result_list.append(item_dict)

            return jsonify(result_list), HTTPStatus.OK

        except sqlalchemy.exc.NoResultFound:
            return {'Error': 'Harbor not found'}, HTTPStatus.NOT_FOUND
    else:
        return {'msg': 'You are a company user. You are not allowed to handle harbors data.'}, HTTPStatus.UNAUTHORIZED


@jwt_required()
def get_ships_on_harbor_all_times(harbor_name:str):

    current_username = get_jwt_identity()['username']
    user = User.query.filter_by(username=current_username).first()

    if user.is_harbor:
        try:
            harbor = Harbor.query.filter_by(name=harbor_name.capitalize()).one()
            
            result_list = []
            
            for item in harbor.ships:
                item_dict = asdict(item)
                item_dict['dates_in_harbor'] = [{
                    'entry_date': item.entry_date, 
                    'exit_date': item.exit_date                      
                    } for item in item.ship_harbor_dates]

                result_list.append(item_dict)
            
            return jsonify(result_list), HTTPStatus.OK

        except sqlalchemy.exc.NoResultFound:
            return {'Error': 'Harbor not found'}, HTTPStatus.NOT_FOUND
    else:
        return {'msg': 'You are a company user. You are not allowed to handle harbors data.'}, HTTPStatus.UNAUTHORIZED


@jwt_required()
def update_ships_on_harbor(harbor_name:str):

    current_username = get_jwt_identity()['username']
    user = User.query.filter_by(username=current_username).first()

    data = request.json

    if user.is_harbor:
        try:
            harbor = Harbor.query.filter_by(name=harbor_name.capitalize()).first()
            ship = Ship.query.filter_by(name=data['ship']).first()

            ship_harbor_item = ShipHarbor.query.filter(ShipHarbor.id_ship == ship.id_ship)\
                .order_by(ShipHarbor.id_ship_harbor.desc()).first()

            if ship_harbor_item and ship_harbor_item.exit_date == None:
                ship_harbor_item.exit_date = datetime.utcnow()

                current_app.db.session.commit()

                ship_harbor_item = ShipHarbor.query.filter(ShipHarbor.id_ship == ship.id_ship)\
                .order_by(ShipHarbor.id_ship_harbor.desc()).first()

                new_item = {'ship': ship.name,
                            'entry_date': ship_harbor_item.entry_date,
                            'exit_date': ship_harbor_item.exit_date
                            }

                return jsonify(new_item), HTTPStatus.OK
            
            elif not ship_harbor_item or ship_harbor_item.exit_date != None:

                ship_entry_date = datetime.utcnow()
                item = ShipHarbor(entry_date=ship_entry_date)
                item.ship = ship
                harbor.ship_harbor_items.append(item)
                
                current_app.db.session.commit()

                ship_harbor_item = ShipHarbor.query.filter(ShipHarbor.id_ship == ship.id_ship)\
                .order_by(ShipHarbor.id_ship_harbor.desc()).first()

                new_item = {'ship': ship.name,                        
                            'entry_date': ship_harbor_item.entry_date,
                            'exit_date': None
                            }

                return jsonify(new_item), HTTPStatus.OK
        
        except AttributeError:
            return {'Error': 'Ship not found'}, HTTPStatus.NOT_FOUND     
    else:
        return {'msg': 'You are a company user. You are not allowed to handle harbors data.'}, HTTPStatus.UNAUTHORIZED

