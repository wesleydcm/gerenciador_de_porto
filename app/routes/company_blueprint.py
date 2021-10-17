from sys import path
from flask import Blueprint
from app.controllers.company_controller import (
    get_company, register_company, update
)

bp = Blueprint('company_bp', __name__, url_prefix='/shipping_company')

bp.post("")(register_company)
bp.get("<string:trading_name>")(get_company)
bp.patch("<string:trading_name>")(update)
