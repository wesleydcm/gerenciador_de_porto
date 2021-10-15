from flask import Blueprint
from app.controllers.navio_controller import get_one_ship

bp = Blueprint('ship_bp', __name__, url_prefix='/ship')

bp.get('int:id')(get_one_ship)
