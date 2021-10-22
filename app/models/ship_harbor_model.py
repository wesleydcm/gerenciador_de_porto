from datetime import date
from sqlalchemy import Column, Integer, DateTime
from dataclasses import dataclass
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.configs.database import db


@dataclass
class ShipHarbor(db.Model):

    entry_date: datetime
    exit_date: datetime

    __tablename__ = "ship_harbor"

    id_ship_harbor = Column(Integer, primary_key=True)
    entry_date = Column(DateTime)
    exit_date = Column(DateTime)
    id_ship = Column(
        Integer, ForeignKey("ships.id_ship", ondelete="cascade")
    )
    id_harbor = Column(
        Integer, ForeignKey("harbor.id_harbor", ondelete="cascade")
    )

    ship = relationship('Ship', backref='ship_harbor_dates')

