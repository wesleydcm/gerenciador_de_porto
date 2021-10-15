from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.schema import ForeignKey
from dataclasses import dataclass

from app.configs.database import db


@dataclass
class ViagemModel(db.Model):
    destino: str
    codigo: str

    __tablename__ = "viagens"

    id_viagem = Column(Integer, primary_key=True)
    destino = Column(String, nullable=False, unique=True)
    codigo = Column(Integer, nullable=False, unique=True)
    id_navio = Column(
        Integer, ForeignKey("navios.id_navio", ondelete="cascade")
    )
