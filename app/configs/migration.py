from flask import Flask
from flask_migrate import Migrate


def init_app(app:Flask):

    # from app.models.container_model import
    # from app.models.container_porto_model import
    # from app.models.container_viagem_model import
    # from app.models.empresa_model import 
    # from app.models.navio_model import
    # from app.models.navio_porto_model import
    # from app.models.porto_model import
    # from app.models.usuario_model import
    # from app.models.viagem_model import

    Migrate(app, app.db)

