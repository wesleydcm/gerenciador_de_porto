from http import HTTPStatus
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from app.models.user_model import User
from flask import jsonify, request, current_app


def session(model, action):
    """
        receives the object and an write the action
        to "add" to add to db
        or "remove" to delete from the db
    """
    session = current_app.db.session()

    if action == "add":
        session.add(model)
        session.commit()

    elif action == "remove":
        session.delete(model)
        session.commit()


def register_user():
    data = request.get_json()
    new_user = User(**data)
    session(new_user, "add")

    return jsonify(new_user), HTTPStatus.CREATED


def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()

    if user.check_password(data["password"]):
        access_token = create_access_token(user)
        return {"access_token": access_token}, HTTPStatus.OK

    return {"Error": "Bad username or password"}, HTTPStatus.BAD_REQUEST


@jwt_required()
def get_user():
    user = get_jwt_identity()

    new_user = User.query.filter_by(id_user=user["id_user"]).first()

    if not user:
        return {'msg': 'user not found'}, HTTPStatus.BAD_REQUEST

    return jsonify(new_user), HTTPStatus.OK


@jwt_required()
def update():
    data = request.get_json()
    user_data = get_jwt_identity()

    user = User.query.filter_by(username=user_data["username"]).first()

    if data["password"]:
        password_to_hash = data.pop("password")
        user.password = password_to_hash
        current_app.db.session.commit()

    if data:
        for key, value in data.items():
            setattr(user, key, value)

        User.query.filter_by(username=user_data["username"]).update(data)
        current_app.db.session.commit()

    return jsonify(user), HTTPStatus.OK


@jwt_required()
def delete():
    data_user = get_jwt_identity()
    user = User.query.filter_by(username=data_user["username"]).first()
    session(user, "remove")

    return jsonify(user), HTTPStatus.OK
