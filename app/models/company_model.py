from sqlalchemy.orm import relationship
from app.configs.database import db
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql.schema import ForeignKey
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ShippingCompany(db.Model):

    created_at: datetime
    trading_name: str

    __tablename__ = 'shipping_company'

    id_shipping_company = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False)
    trading_name = Column(String(255), nullable=False, unique=True)
    id_user = Column(Integer, ForeignKey('users.id_user', ondelete='cascade'))

    containers = relationship("Container", backref="company")
    ships = relationship("Ship", backref="company")

