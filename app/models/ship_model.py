from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey


@dataclass
class Ship(db.Model):
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
            "shipping_company.id_empresa_maritima", ondelete="cascade"
        )
    )
