from dataclasses import dataclass, asdict, astuple

from app.configs.database import db
from app.controllers.utils import generate_random_alphanumeric
from app.models.company_model import ShippingCompany
from app.models.ship_model import Ship
from flask import current_app
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.elements import and_
from sqlalchemy.sql.schema import ForeignKey

from app.models.user_model import User


@dataclass
class Travel(db.Model):

    travel_code: str
    destination: str
    id_ship: int

    __tablename__ = "travel"

    id_travel = Column(Integer, primary_key=True)
    travel_code = Column(String(127), nullable=False, unique=True)
    destination = Column(String(63), nullable=False)
    id_ship = Column(
        Integer, ForeignKey("ships.id_ship", ondelete="cascade")
    )

    def generate_travel_code(self):

        length_travel_code = 6

        query = current_app.db.session\
            .query(Travel.travel_code)\
            .select_from(Travel)\
            .all()
        
        existing_travel_codes = [code[0] for code in query]

        while True:
            new_code = generate_random_alphanumeric(length_travel_code)

            if new_code not in existing_travel_codes:
                break

        self.travel_code = new_code


    def check_authorization(self, requester_username):

        session = current_app.db.session

        query = session.query(Ship, ShippingCompany, User)\
            .select_from(Ship)\
            .join(ShippingCompany)\
            .join(User)\
            .filter(and_(
                Ship.id_ship == self.id_ship),
                ShippingCompany.id_shipping_company == Ship.id_shipping_company,\
                ShippingCompany.id_shipping_company == User.id_user,
                )\
            .all()

        owner_travel = [asdict(username) for _, _, username in query][0]

        if requester_username != owner_travel['username']:
            raise PermissionError("You must be the owner of the trip to make changes or view the information.")
