from app.controllers.container_controller import get_one_container, list_containers
from flask import Blueprint

bp = Blueprint('container_bp', __name__, url_prefix='/containers')

bp.get('')(list_containers)
bp.get('/<int:id_container>')(get_one_container)
