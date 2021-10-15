from app.controllers.travel_controller import get_one_travel
from flask import Blueprint

bp = Blueprint('travel_bp', __name__, url_prefix='/travel')

bp.get('/<int:id>')(get_one_travel)
