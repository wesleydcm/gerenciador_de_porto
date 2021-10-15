from sqlalchemy import Column, String, Integer
from dataclasses import dataclass
from sqlalchemy.sql.schema import ForeignKey

from app.configs.database import db


@dataclass
class NavioModel(db.Model):
    nome: str
    calado: int
    tamanho: int
    nacionalidade: str

    __tablename__ = "navios"

    id_navio = Column(Integer, primary_key=True)
    nome = Column(String(256), nullable=False, unique=True)
    calado = Column(Integer, nullable=False)
    tamanho = Column(Integer, nullable=False)
    nacionalidade = Column(String(50), nullable=False)
    id_empresa_maritima = Column(
        Integer, ForeignKey(
            "empresa_maritima.id_empresa_maritima", ondelete="cascade"
        )
    )
