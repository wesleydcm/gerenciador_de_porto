import datetime
from sqlalchemy.orm import relationship
from app.configs.database import db
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql.schema import ForeignKey
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ContainerHarbor(db.Model):

    entry_date: datetime
    exit_date: datetime

    __tablename__ = 'container_harbor'

    id_container_travel = Column(Integer, primary_key=True)
    entry_date = Column(DateTime, nullable=False)
    exit_date = Column(DateTime)
    id_container = Column(Integer, ForeignKey('containers.id_container', ondelete='cascade'))
    id_harbor = Column(Integer, ForeignKey('harbor.id_harbor', ondelete='cascade'))

    container = relationship('Container')
