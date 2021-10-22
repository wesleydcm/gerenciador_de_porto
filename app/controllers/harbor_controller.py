from dataclasses import asdict

<<<<<<< HEAD
from app.models.harbor_model import Harbor
from flask import current_app, jsonify, request
=======
            session = current_app.db.session
            query_list = session.query(Container.tracking_code,\
                                       ContainerHarbor.entry_date,\
                                       sqlalchemy.func.max(ContainerHarbor.exit_date))\
                                       .join(Container, Container.id_container == ContainerHarbor.id_container)\
                                       .filter(ContainerHarbor.id_harbor == harbor.id_harbor)\
                                       .group_by(Container.tracking_code, ContainerHarbor.entry_date)\
                                       .all()

            result_list = [{'container': query[0], 
                            'entry_date': query[1],
                            'exit_date': query[2]} 
                            for query in query_list]
            
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
            
            session = current_app.db.session
            query_list = session.query(Ship.name,\
                                       ShipHarbor.entry_date,\
                                       sqlalchemy.func.max(ShipHarbor.exit_date))\
                                       .join(Ship, Ship.id_ship == ShipHarbor.id_ship)\
                                       .filter(ShipHarbor.id_harbor == harbor.id_harbor)\
                                       .group_by(Ship.name, ShipHarbor.entry_date)\
                                       .all()

            result_list = [{'ship': query[0], 
                            'entry_date': query[1]} 
                            for query in query_list if query[2] == None]

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
            session = current_app.db.session
            query_list = session.query(Ship.name,\
                                       ShipHarbor.entry_date,\
                                       sqlalchemy.func.max(ShipHarbor.exit_date))\
                                       .join(Ship, Ship.id_ship == ShipHarbor.id_ship)\
                                       .filter(ShipHarbor.id_harbor == harbor.id_harbor)\
                                       .group_by(Ship.name, ShipHarbor.entry_date)\
                                       .all()

            result_list = [{'ship': query[0], 
                            'entry_date': query[1],
                            'exit_date': query[2]} 
                            for query in query_list]
            
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
>>>>>>> 65b82ccff00bfa2661198cd9fd23f6a5ec6fa7c6


def get_one_harbor(id:int):

    harbor = Harbor.query.get(id)

    if not harbor:
        return {'msg': 'harbor not found'}, 404
    
    return jsonify(harbor), 200
