from http import HTTPStatus

from app.models.company_model import ShippingCompany
from app.models.container_model import Container
from flask import current_app, jsonify, request


def get_one_company(id: int):

    company = ShippingCompany.query.get(id)

    if not company:
        return {'msg': 'shipping company not found'}, 404
    
    return jsonify(company), 200


def list_containers_by_company(id: int):

    company: ShippingCompany = ShippingCompany.query.get(id)

    containers = Container.query.filter_by(id_shipping_company = company.id_shipping_company).all()

    if not containers:
        return {'msg': "company does not have registered containers"}, HTTPStatus.NOT_FOUND

    return jsonify(containers), HTTPStatus.OK
