from app.configs.database import db
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.sql.schema import ForeignKey
from dataclasses import dataclass


@dataclass
class ShippingCompany(db.Model):

    created_at: Date
    trading_name: str

    __tablename__ = 'shipping_company'

    id_shipping_company = Column(Integer, primary_key=True)
    created_at = Column(Date, nullable=False)
    trading_name = Column(String(255), nullable=False, unique=True)
    id_user = Column(Integer, ForeignKey('users.id_user', ondelete='cascade'))
