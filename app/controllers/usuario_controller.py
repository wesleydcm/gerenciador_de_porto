from flask import request, jsonify, current_app
from app.models.usuario_model import UsuarioModel
from dataclasses import asdict


def get_one_user(id:int):

    user = UsuarioModel.query.get(id)
    
    return jsonify(user), 200

    