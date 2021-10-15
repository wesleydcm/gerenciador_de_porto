from flask import Blueprint
from app.controllers.harbor_controller import get_one_harbor

bp = Blueprint('harbor_bp', __name__, url_prefix='/harbor')

bp.get('/<int:id>')(get_one_harbor)
