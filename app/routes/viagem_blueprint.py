from flask import Blueprint
from app.controllers.viagem_controller import get_one_travel

bp = Blueprint('travel_bp', __name__, url_prefix='/travel')

bp.get('int:id')(get_one_travel)
