from flask import jsonify, request, current_app
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from flask_jwt_extended import (
    create_access_token, jwt_required, get_jwt_identity
)

from app.models.user_model import User
from app.controllers.utils import session


def register_user():
    try:
        data = request.get_json()
        new_user = User(**data)
        session(new_user, "add")

        return {"msg": "User created!"}, HTTPStatus.CREATED

    except IntegrityError as err:
        message = str(str(err.orig).split("\n")[0]).split()
        return {"Error": " ".join(message[:5])}, HTTPStatus.BAD_REQUEST

    except TypeError as err:
        return {"Error": str(err)}


def login():
    try:
        data = request.get_json()
        user = User.query.filter_by(username=data["username"]).first()

        if user.check_password(data["password"]):
            access_token = create_access_token(user)
            return {"access_token": access_token}, HTTPStatus.OK

        return {"Error": "Bad username or password"}, HTTPStatus.BAD_REQUEST

    except AttributeError:
        return {
            "Error": "Username or password invalid!"
        }, HTTPStatus.BAD_REQUEST


@jwt_required()
def get_user():
    user = get_jwt_identity()

    new_user = User.query.filter_by(username=user["username"]).first()

    if not user:
        return {'msg': 'user not found'}, HTTPStatus.BAD_REQUEST

    return jsonify(new_user), HTTPStatus.OK


@jwt_required()
def update():
    try:
        data = request.get_json()
        user_data = get_jwt_identity()

        user = User.query.filter_by(username=user_data["username"]).first()

        if data.get("password"):
            password_to_hash = data.pop("password")
            user.password = password_to_hash
            current_app.db.session.commit()

        if data:
            for key, value in data.items():
                setattr(user, key, value)

            User.query.filter_by(username=user_data["username"]).update(data)
            current_app.db.session.commit()

        return jsonify(user), HTTPStatus.OK

    except InvalidRequestError as err:
        # TODO: tratar a mensagem do erro
        return {"Error": str(err)}


@jwt_required()
def delete():
    data_user = get_jwt_identity()
    user = User.query.filter_by(username=data_user["username"]).first()
    session(user, "remove")

    return jsonify(user), HTTPStatus.OK
