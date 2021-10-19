from app.models.user_model import User
from app.models.harbor_model import Harbor
from app.models.ship_harbor_model import ShipHarbor
from app.models.ship_model import Ship
from app.models.container_harbor_model import ContainerHarbor
from app.models.container_model import Container
from app.controllers.utils import session
from flask import jsonify, request, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from http import HTTPStatus
import psycopg2
import sqlalchemy


@jwt_required()
def create_harbor():
    current_username = get_jwt_identity()['username']
    user = User.query.filter_by(username=current_username).first()

    if user.is_harbor:

        try:

            data = request.json

            if data.get('teus') == None:
                return {"msg": "null value in column \"teus\" of relation \"harbor\" violates not-null constraint"}, HTTPStatus.BAD_REQUEST

            if data.get('name') == None:
                return {"msg": "null value in column \"name\" of relation \"harbor\" violates not-null constraint"}, HTTPStatus.BAD_REQUEST
            
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
                return {'msg': str(e.orig).split('\n')[0]}, HTTPStatus.BAD_REQUEST

            return {'msg': str(e).split('\n')[1]}, HTTPStatus.CONFLICT

        except TypeError as e:
             return {'msg': str(e)}, HTTPStatus.BAD_REQUEST

    else:
        return {'msg': 'You are a company user. You are not allowed to handle harbors data.'}, HTTPStatus.UNAUTHORIZED
            

@jwt_required()
def get_one_harbor(harbor_name:str):

    current_username = get_jwt_identity()['username']
    user = User.query.filter_by(username=current_username).first()

    if user.is_harbor:
        try:
            harbor = Harbor.query.filter_by(name=harbor_name.capitalize()).first()
            return jsonify(harbor), HTTPStatus.OK

        except AttributeError:
            return {'msg': 'Harbor not found'}, HTTPStatus.NOT_FOUND
    else:
        return {'msg': 'You are a company user. You are not allowed to handle harbors data.'}, HTTPStatus.UNAUTHORIZED
        
        
@jwt_required()
def delete_one_harbor(harbor_name:str):

    current_username = get_jwt_identity()['username']
    user = User.query.filter_by(username=current_username).first()

    if user.is_harbor:
        try:
            harbor = Harbor.query.filter_by(name=harbor_name.capitalize()).first()
            session(harbor, "remove")

            return {"msg": f'Harbor {harbor.name} no longer exists.'}, HTTPStatus.NO_CONTENT

        except AttributeError:
            return {'msg': 'Harbor not found'}, HTTPStatus.NOT_FOUND
    else:
         return {'msg': 'You are a company user. You are not allowed to handle harbors data.'}, HTTPStatus.UNAUTHORIZED


@jwt_required()
def update_one_harbor(harbor_name:str):

    current_username = get_jwt_identity()['username']
    user = User.query.filter_by(username=current_username).first()

    data = request.json   

    if user.is_harbor:
        try:
            harbor = Harbor.query.filter_by(name=harbor_name.capitalize()).first()

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
            
        except AttributeError:
            return {'msg': 'Harbor not found'}, HTTPStatus.NOT_FOUND

        except sqlalchemy.exc.IntegrityError as e:
            return {'msg': str(e).split('\n')[1]}, HTTPStatus.CONFLICT

        except sqlalchemy.exc.InvalidRequestError as e:
            return {'msg': str(e)}, HTTPStatus.BAD_REQUEST    
    else:
        return {'msg': 'You are a company user. You are not allowed to handle harbors data.'}, HTTPStatus.UNAUTHORIZED


@jwt_required()
def get_containers_on_harbor_now(harbor_name:str):

    current_username = get_jwt_identity()['username']
    user = User.query.filter_by(username=current_username).first()

    if user.is_harbor:
        try:
            harbor = Harbor.query.filter_by(name=harbor_name.capitalize()).first()

            container_harbor_list = ContainerHarbor.query.filter(ContainerHarbor.id_harbor == harbor.id_harbor,
                ContainerHarbor.exit_date == None).all()

            result_list = []

            for container_harbor in container_harbor_list:
                
                container_dict = {
                    'container': container_harbor.container.tracking_code, 
                    'entry_date': container_harbor.entry_date,
                    'exit_date': container_harbor.exit_date 
                    }
                result_list.append(container_dict)
            
            return jsonify(result_list), HTTPStatus.OK

        except AttributeError:
            return {'msg': 'Harbor not found'}, HTTPStatus.NOT_FOUND
    else:
        return {'msg': 'You are a company user. You are not allowed to handle harbors data.'}, HTTPStatus.UNAUTHORIZED


@jwt_required()
def get_containers_on_harbor_all_times(harbor_name:str):

    current_username = get_jwt_identity()['username']
    user = User.query.filter_by(username=current_username).first()

    if user.is_harbor:
        try:
            harbor = Harbor.query.filter_by(name=harbor_name.capitalize()).first()
    
            container_harbor_list = ContainerHarbor.query.filter(ContainerHarbor.id_harbor == harbor.id_harbor,
                ContainerHarbor.exit_date == None).all()

            result_list = []

            for container_harbor in container_harbor_list:
                
                container_dict = {
                    'container': container_harbor.container.tracking_code, 
                    'entry_date': container_harbor.entry_date,
                    'exit_date': container_harbor.exit_date  
                    }
                result_list.append(container_dict)
            
            return jsonify(result_list), HTTPStatus.OK

        except AttributeError:
            return {'msg': 'Harbor not found'}, HTTPStatus.NOT_FOUND
    else:
        return {'msg': 'You are a company user. You are not allowed to handle harbors data.'}, HTTPStatus.UNAUTHORIZED


@jwt_required()
def update_containers_on_harbor(harbor_name:str):

    current_username = get_jwt_identity()['username']
    user = User.query.filter_by(username=current_username).first()

    data = request.json

    if user.is_harbor:

        harbor = Harbor.query.filter_by(name=harbor_name.capitalize()).first()
        container = Container.query.filter_by(tracking_code=data['tracking_code']).first()

        if data.get('entry_date'):

            item = ContainerHarbor(entry_date=data['entry_date'])
            item.container = container
            harbor.container_harbor_items.append(item)
            harbor.availability -= container.teu

            current_app.db.session.commit()

            new_item = {'container': container.tracking_code,                        
                        'entry_date': harbor.container_harbor_items.entry_date,
                        'exit_date': None
                        }

            return jsonify(new_item), HTTPStatus.OK

        elif data.get('exit_date'):

            container_harbor_item = ContainerHarbor.query.filter(ContainerHarbor.id_container == container.id_container,
                ContainerHarbor.exit_date == None).first()

            data['entry_date'] = container_harbor_item.entry_date
            item = ContainerHarbor(entry_date=data['entry_date'], exit_date=data['exit_date'])
            item.container = container
            harbor.container_harbor_items.append(item)
            harbor.availability += container.teu

            current_app.db.session.commit()

            new_item = {'container': container.tracking_code,                        
                        'entry_date': harbor.container_harbor_items.entry_date,
                        'exit_date': harbor.container_harbor_items.exit_date
                        }

            return jsonify(new_item), HTTPStatus.OK
    else:
        return {'msg': 'You are a company user. You are not allowed to handle harbors data.'}, HTTPStatus.UNAUTHORIZED


@jwt_required()
def get_ships_on_harbor_now(harbor_name:str):

    current_username = get_jwt_identity()['username']
    user = User.query.filter_by(username=current_username).first()

    if user.is_harbor:
        try:
            harbor = Harbor.query.filter_by(name=harbor_name.capitalize()).first()
            ship_harbor_list = ShipHarbor.query.filter(ShipHarbor.id_harbor == harbor.id_harbor,
                    ShipHarbor.exit_date == None).all()

            result_list = []

            for ship_harbor in ship_harbor_list:            
                ship_dict = {
                    'ship': ship_harbor.ship.name, 
                    'entry_date': ship_harbor.entry_date,
                    'exit_date': ship_harbor.exit_date 
                    }
                result_list.append(ship_dict)
            
            return jsonify(result_list), HTTPStatus.OK

        except AttributeError:
            return {'msg': 'Ship not found'}, HTTPStatus.NOT_FOUND
    else:
        return {'msg': 'You are a company user. You are not allowed to handle harbors data.'}, HTTPStatus.UNAUTHORIZED


@jwt_required()
def get_ships_on_harbor_all_times(harbor_name:str):

    current_username = get_jwt_identity()['username']
    user = User.query.filter_by(username=current_username).first()

    if user.is_harbor:
        try:
            harbor = Harbor.query.filter_by(name=harbor_name.capitalize()).first()
            ship_harbor_list = ShipHarbor.query.filter(ShipHarbor.id_harbor == harbor.id_harbor,
                    ShipHarbor.exit_date == None).all()

            result_list = []

            for ship_harbor in ship_harbor_list:            
                ship_dict = {
                    'ship': ship_harbor.ship.name, 
                    'entry_date': ship_harbor.entry_date,
                    'exit_date': ship_harbor.exit_date  
                    }
                result_list.append(ship_dict)
            
            return jsonify(result_list), HTTPStatus.OK

        except AttributeError:
            return {'msg': 'Ship not found'}, HTTPStatus.NOT_FOUND
    else:
        return {'msg': 'You are a company user. You are not allowed to handle harbors data.'}, HTTPStatus.UNAUTHORIZED


@jwt_required()
def update_ships_on_harbor(harbor_name:str):

    current_username = get_jwt_identity()['username']
    user = User.query.filter_by(username=current_username).first()

    data = request.json

    if user.is_harbor:
        harbor = Harbor.query.filter_by(name=harbor_name.capitalize()).first()
        ship = Ship.query.filter_by(name=data['name']).first()

        if data.get('entry_date'):

            item = ShipHarbor(entry_date=data['entry_date'])
            item.ship = ship
            harbor.ship_harbor_items.append(item)
            current_app.db.session.commit()

            new_item = {'ship': ship.name,                        
                        'entry_date': harbor.ship_harbor_items.entry_date,
                        'exit_date': None
                        }

            return jsonify(new_item), HTTPStatus.OK

        elif data.get('exit_date'):

            ship_harbor_item = ShipHarbor.query.filter(ShipHarbor.id_ship == ship.id_ship,
                ShipHarbor.exit_date == None).all()
            data['entry_date'] = ship_harbor_item.entry_date
            item = ContainerHarbor(entry_date=data['entry_date'], exit_date=data['exit_date'])
            item.ship = ship
            harbor.ship_harbor_items.append(item)

            current_app.db.session.commit()

            new_item = {'ship': ship.name,
                        'entry_date': ship.container_harbor_items.entry_date,
                        'exit_date': ship.container_harbor_items.exit_date
                        }

            return jsonify(new_item), HTTPStatus.OK
    else:
        return {'msg': 'You are a company user. You are not allowed to handle harbors data.'}, HTTPStatus.UNAUTHORIZED



