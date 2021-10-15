from sqlalchemy import Column, String, Integer
from dataclasses import dataclass

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
