<<<<<<< HEAD
=======
from dataclasses import dataclass
from app.configs.database import db
>>>>>>> b51ba58c0ca82d4bb665479167fc3c56550de9a8
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db
from dataclasses import dataclass


@dataclass
class Travel(db.Model):

    travel_code: str
    destination: str
    id_ship: int

    __tablename__ = "travel"

    id_travel = Column(Integer, primary_key=True)
    travel_code = Column(String(127), nullable=True, unique=True)
    destination = Column(String(63), nullable=False)
    id_ship = Column(
        Integer, ForeignKey("ships.id_ship", ondelete="cascade")
    )

