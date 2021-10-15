from sqlalchemy import Column, String, Integer
from dataclasses import dataclass

from app.configs.database import db


@dataclass
class UsuarioModel(db.Model):
    nome: str
    username: str

    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False, unique=True)
    senha = Column(String(127), nullable=False)
