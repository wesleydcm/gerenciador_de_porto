from flask import Blueprint
from app.controllers.company_controller import get_one_company, list_containers_by_company

bp = Blueprint('company_bp', __name__, url_prefix='/shipping_company')

bp.get('/<int:id>')(get_one_company)
bp.get('/<int:id>/containers')(list_containers_by_company)