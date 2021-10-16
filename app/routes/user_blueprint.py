from app.controllers.user_controller import register_user, login ,get_one_user
from flask import Blueprint

bp = Blueprint('user_bp', __name__, url_prefix='/users')

bp.post("")(register_user)
bp.post("/login")(login)
bp.get('/<int:id>')(get_one_user)
