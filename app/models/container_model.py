from app.configs.database import db
from sqlalchemy import Column, Integer, String
from dataclasses import dataclass


@dataclass
class ContainerModel (db.Model):

    codigo_rastreio: int
    teu: int
    tipo: str
    
    __tablename__ = 'containers'

    id_container = Column(Integer, primary_key=True)
    codigo_rastreio = Column(String(100), nullable=False, unique=True)
    teu = Column(Integer, nullable=False, default=1)
    tipo = Column(String(255), nullable=False, default='dry box')
    