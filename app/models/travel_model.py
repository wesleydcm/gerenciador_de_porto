from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey


@dataclass
class Travel(db.Model):

    destination: str
    code: str

    __tablename__ = "travel"

    id_viagem = Column(Integer, primary_key=True)
    destination = Column(String, nullable=False, unique=True)
    code = Column(Integer, nullable=False, unique=True)
    id_ship = Column(
        Integer, ForeignKey("ships.id_ship", ondelete="cascade")
    )
