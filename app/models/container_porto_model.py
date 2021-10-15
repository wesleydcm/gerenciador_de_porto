from app.configs.database import db
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.sql.schema import ForeignKey
from dataclasses import dataclass


@dataclass
class ContainerPortoModel (db.Model):

    data_entrada: Date
    data_saida: Date
    
    __tablename__ = 'container_porto'

    id_container_viagem = Column(Integer, primary_key=True)
    data_entrada = Column(Date, nullable=False)
    data_saida = Column(Date)
    id_container = Column(Integer, ForeignKey('containers.id_container', ondelete='cascade'))
    id_porto = Column(Integer, ForeignKey('porto.id_porto', ondelete='cascade'))

