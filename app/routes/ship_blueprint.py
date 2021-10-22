from app.controllers.ship_controller import (
    create_ship, info_ship, update_ship, delete_ship, all_ship_travel, ship_locate
)
from flask import Blueprint

bp = Blueprint('ship_bp', __name__, url_prefix='/ship')

bp.post('')(create_ship)
bp.get('/<string:name_ship>')(info_ship)
bp.patch('/<string:name_ship>')(update_ship)
bp.delete('/<string:name_ship>')(delete_ship)
bp.get('/<string:name_ship>/travels')(all_ship_travel)
bp.get('/<string:name_ship>/locate')(ship_locate)

