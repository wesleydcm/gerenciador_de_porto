from flask import Blueprint
from app.controllers.usuario_controller import get_one_user

bp = Blueprint('user_bp', __name__, url_prefix='/user')

bp.get('int:id')(get_one_user)
