from sqlalchemy import Column, String, Integer
from dataclasses import dataclass

from app.configs.database import db


@dataclass
class PortoModel(db.Model):
    nome: str
    pais: str
    cidade: str
    teus: int
    disponibilidade: int

    __tablename__ = "usuarios"

    id_porto = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False, unique=True)
    pais = Column(String(255), nullable=False)
    cidade = Column(String(255), nullable=False)
    teus = Column(Integer, nullable=False)
    disponibilidade = Column(Integer, nullable=False)
