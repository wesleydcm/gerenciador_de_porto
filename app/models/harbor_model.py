from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from dataclasses import dataclass
from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db


@dataclass
class Harbor(db.Model):
    name: str
    country: str
    city: str
    teus: int
    availability: int

    __tablename__ = "harbor"

    id_harbor = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    country = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    teus = Column(Integer, nullable=False)
    availability = Column(Integer, nullable=False)
    id_user = Column(
        Integer, ForeignKey("users.id_user", ondelete="cascade")
    )

    user = relationship('User', backref='harbor')

    container_harbor_items = relationship(
        'ContainerHarbor', cascade='all, delete-orphan'
    )

    ship_harbor_items = relationship(
        'ShipHarbor', cascade='all, delete-orphan'
    )
