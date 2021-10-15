from dataclasses import asdict

from app.models.company_model import ShippingCompany
from flask import current_app, jsonify, request


def get_one_company(id:int):

    company = ShippingCompany.query.get(id)

    if not company:
        return {'msg': 'ship company not found'}, 404
    
    return jsonify(company), 200
