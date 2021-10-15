from flask import Flask
from flask_migrate import Migrate


def init_app(app:Flask):

    from app.models.user_model import User
    from app.models.harbor_model import Harbor
    from app.models.company_model import ShippingCompany
    from app.models.container_model import Container
    from app.models.ship_model import Ship
    from app.models.travel_model import Travel
    from app.models.ship_harbor_model import ShipHarbor
    from app.models.container_travel_model import ContainerTravel
    from app.models.container_harbor_model import ContainerHarbor

    Migrate(app, app.db)
