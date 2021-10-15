from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey


@dataclass
class Travel(db.Model):
    destino: str
    codigo: str

    __tablename__ = "viagens"

    id_viagem = Column(Integer, primary_key=True)
    destino = Column(String, nullable=False, unique=True)
    codigo = Column(Integer, nullable=False, unique=True)
    id_navio = Column(
        Integer, ForeignKey("navios.id_navio", ondelete="cascade")
    )
