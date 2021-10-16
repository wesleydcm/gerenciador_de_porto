from http import HTTPStatus

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


def get_one_user(id:int):

    user = User.query.get(id)

    if not user:
        return {'msg': 'user not found'}, 404
    return jsonify(user), 200
