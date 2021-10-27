<<<<<<< HEAD
=======
from dataclasses import dataclass
from app.configs.database import db
>>>>>>> b51ba58c0ca82d4bb665479167fc3c56550de9a8
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from app.configs.database import db
from dataclasses import dataclass


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

    travel = relationship("Travel", backref="ship")

    harbors = relationship('Harbor',
                           secondary='ship_harbor', backref='ships')
