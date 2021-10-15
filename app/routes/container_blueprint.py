from app.controllers.container_controller import get_one_container
from flask import Blueprint

bp = Blueprint('container_bp', __name__, url_prefix='/container')

bp.get('/<int:id>')(get_one_container)
