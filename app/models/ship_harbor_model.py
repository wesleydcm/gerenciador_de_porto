from datetime import date
from sqlalchemy import Column, Date, Integer
from dataclasses import dataclass
from sqlalchemy.sql.schema import ForeignKey

from app.configs.database import db


@dataclass
class ShipHarbor(db.Model):

    entry_date: date
    exit_date: date

    __tablename__ = "ship_harbor"

    id_ship_harbor = Column(Integer, primary_key=True)
    entry_date = Column(Date)
    exit_date = Column(Date)
    id_ship = Column(
        Integer, ForeignKey("ships.id_ship", ondelete="cascade")
    )
    id_harbor = Column(
        Integer, ForeignKey("harbor.id_harbor", ondelete="cascade")
    )
