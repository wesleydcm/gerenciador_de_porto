from flask import Flask
from flask_migrate import Migrate


def init_app(app:Flask):

    from app.models.container_model import ContainerModel
    from app.models.container_porto_model import ContainerPortoModel
    from app.models.container_viagem_model import ContainerViagemModel
    from app.models.empresa_model import EmpresaMaritimaModel 
    from app.models.navio_model import NavioModel
    from app.models.navio_porto_model import NavioPortoModel
    from app.models.porto_model import PortoModel
    from app.models.usuario_model import UsuarioModel
    from app.models.viagem_model import ViagemModel

    Migrate(app, app.db)

