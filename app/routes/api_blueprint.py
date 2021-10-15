from flask import Blueprint
from app.routes import container_blueprint, empresa_blueprint, navio_blueprint, harbor_blueprint, usuario_blueprint, viagem_blueprint

bp = Blueprint('harbor_manager_bp', __name__, url_prefix='/harbor_manager')

bp.register_blueprint(container_blueprint.bp)
bp.register_blueprint(empresa_blueprint.bp)
bp.register_blueprint(navio_blueprint.bp)
bp.register_blueprint(harbor_blueprint.bp)
bp.register_blueprint(usuario_blueprint.bp)
bp.register_blueprint(viagem_blueprint.bp)
