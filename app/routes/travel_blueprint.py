from app.controllers.travel_controller import delete_travel, get_by_travel_code, register_travel, update_travel
from flask import Blueprint

bp = Blueprint('travel_bp', __name__, url_prefix='/travel')


travel_code: str = '/<string:travel_code>'

bp.post('')(register_travel)
bp.get(travel_code)(get_by_travel_code)
bp.patch(travel_code)(update_travel)
bp.delete(travel_code)(delete_travel)