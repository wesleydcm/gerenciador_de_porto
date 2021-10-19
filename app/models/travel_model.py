from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey

from app.controllers.utils import generate_random_alphanumeric


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
        self.travel_code = generate_random_alphanumeric(length_travel_code)
