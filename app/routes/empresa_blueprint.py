from flask import Blueprint
from app.controllers.empresa_controller import get_one_company

bp = Blueprint('company_bp', __name__, url_prefix='/marine_company')

bp.get('/<int:id>')(get_one_company)
