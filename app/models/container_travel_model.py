from app.configs.database import db
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql.schema import ForeignKey
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ContainerTravel(db.Model):

    created_at: datetime
    last_update: datetime

    __tablename__ = 'container_travel'

    id_container_travel = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False)
    last_update = Column(DateTime, nullable=False)
    id_container = Column(
        Integer, ForeignKey('containers.id_container', ondelete='cascade')
    )
    id_travel = Column(
        Integer, ForeignKey('travel.id_travel', ondelete='cascade')
    )
