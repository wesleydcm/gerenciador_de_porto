from dataclasses import asdict
from app.models.harbor_model import Harbor
from flask import current_app, jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity


@jwt_required
def create_harbor():
    
    data = request.json

    harbor_availability = data['teus']

    data['availability'] = harbor_availability

    user_username = get_jwt_identity()['username']

    

    harbor = Harbor(**data)

    session = current_app.db.session
    session.add(harbor)
    session.commit()

    return jsonify(harbor), 201



def get_one_harbor(id:int):

    harbor = Harbor.query.get(id)

    if not harbor:
        return {'msg': 'harbor not found'}, 404
    
    return jsonify(harbor), 200
