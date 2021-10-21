from app.controllers.travel_controller import (
    delete_travel,
    get_all_containers_in_travel,
    get_by_travel_code,
    register_travel,
    update_travel,
    add_container_in_travel
)
from flask import Blueprint

bp = Blueprint('travel_bp', __name__, url_prefix='/travel')

bp.post('')(register_travel)
bp.get('/<string:travel_code>')(get_by_travel_code)
bp.patch('/<string:travel_code>')(update_travel)
bp.delete('/<string:travel_code>')(delete_travel)

bp.post('/<string:travel_code>/add')(add_container_in_travel)
bp.get('/<string:travel_code>/containers')(get_all_containers_in_travel)
