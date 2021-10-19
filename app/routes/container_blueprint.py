from app.controllers.container_controller import (
    create_container, delete_container_by_tracking_code,
    get_container_by_tracking_code, get_every_harbor_container_has_been,
    get_travels_of_container, update_container_by_tracking_code)
from flask import Blueprint

bp = Blueprint('container_bp', __name__, url_prefix='/container')

bp.post('')(create_container)
bp.get('/<int:tracking_code>')(get_container_by_tracking_code)
bp.patch('/<int:tracking_code>')(update_container_by_tracking_code)
bp.delete('/<int:tracking_code>')(delete_container_by_tracking_code)
bp.get('/<int:tracking_code>/travels')(get_travels_of_container)
bp.get('/<int:tracking_code>/harbors')(get_every_harbor_container_has_been)
