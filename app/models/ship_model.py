from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey


@dataclass
class Ship(db.Model):

    name: str
    draught: int
    size: int
    nationality: str

    __tablename__ = "ships"

    id_ship = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False, unique=True)
    draught = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)
    nationality = Column(String(50), nullable=False)
    id_shipping_company = Column(
        Integer, ForeignKey(
            "shipping_company.id_shipping_company", ondelete="cascade"
        )
    )
<<<<<<< HEAD

    travel = relationship("Travel", backref="ship")
=======
>>>>>>> 78197d889ca7011c0075934cf323d8c0d2cd9b7d
