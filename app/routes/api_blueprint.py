from flask import Blueprint
from app.routes import company_blueprint, container_blueprint, harbor_blueprint, ship_blueprint, travel_blueprint, user_blueprint

bp = Blueprint('harbor_manager_bp', __name__, url_prefix='/harbor_manager')

bp.register_blueprint(container_blueprint.bp)
bp.register_blueprint(company_blueprint.bp)
bp.register_blueprint(ship_blueprint.bp)
bp.register_blueprint(harbor_blueprint.bp)
bp.register_blueprint(user_blueprint.bp)
bp.register_blueprint(travel_blueprint.bp)
