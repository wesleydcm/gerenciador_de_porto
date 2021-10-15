from flask import request, jsonify, current_app
from app.models.empresa_model import EmpresaMaritimaModel
from dataclasses import asdict


def get_one_company(id:int):

    company = EmpresaMaritimaModel.query.get(id)
    
    return jsonify(company), 200

    