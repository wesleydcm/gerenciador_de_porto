from datetime import date
from sqlalchemy import Column, Date, Integer
from dataclasses import dataclass
from sqlalchemy.sql.schema import ForeignKey

from app.configs.database import db


@dataclass
class NavioPortoModel(db.Model):
    data_chegada: date
    data_saida: date

    __tablename__ = "navio_porto"

    id_navio_porto = Column(Integer, primary_key=True)
    data_chegada = Column(Date)
    data_saida = Column(Date)
    id_navio = Column(
        Integer, ForeignKey("navios.id_navio", ondelete="cascade")
    )
    id_porto = Column(
        Integer, ForeignKey("porto.id_porto", ondelete="cascade")
    )
