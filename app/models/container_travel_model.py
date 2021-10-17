from app.configs.database import db
from sqlalchemy import Column, Integer, Date
from sqlalchemy.sql.schema import ForeignKey
from dataclasses import dataclass


@dataclass
class ContainerTravel(db.Model):

    created_at: Date
    last_update: Date
    
    __tablename__ = 'container_travel'

    id_container_travel = Column(Integer, primary_key=True)
    created_at = Column(Date, nullable=False)
    last_update = Column(Date, nullable=False)
    id_container = Column(Integer, ForeignKey('containers.id_container', ondelete='cascade'))
    id_travel = Column(Integer, ForeignKey('travel.id_travel', ondelete='cascade'))
