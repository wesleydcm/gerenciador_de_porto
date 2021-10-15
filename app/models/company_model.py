from app.configs.database import db
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.sql.schema import ForeignKey
from dataclasses import dataclass


@dataclass
class ShippingCompany(db.Model):

    data_criacao: Date
    nome_fantasia: str

    __tablename__ = 'shipping_company'

    id_empresa_maritima = Column(Integer, primary_key=True)
    data_criacao = Column(Date, nullable=False)
    nome_fantasia = Column(String(255), nullable=False, unique=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario', ondelete='cascade'))

