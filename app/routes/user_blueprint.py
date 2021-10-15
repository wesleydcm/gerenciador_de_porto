from app.controllers.user_controller import get_one_user
from flask import Blueprint

bp = Blueprint('user_bp', __name__, url_prefix='/user')

bp.get('/<int:id>')(get_one_user)
