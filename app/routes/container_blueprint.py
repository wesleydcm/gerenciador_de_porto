from app.controllers.container_controller import (
    create_container, delete_container_by_tracking_code,
    get_container_by_tracking_code, update_container_by_tracking_code, get_all)
from flask import Blueprint

bp = Blueprint('container_bp', __name__, url_prefix='/container')

bp.post('')(create_container)
bp.get('/<string:tracking_code>')(get_container_by_tracking_code)
bp.get('')(get_all)
bp.patch('/<string:tracking_code>')(update_container_by_tracking_code)
bp.delete('/<string:tracking_code>')(delete_container_by_tracking_code)

