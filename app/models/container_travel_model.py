from app.configs.database import db
from sqlalchemy import Column, Integer, Date
from sqlalchemy.sql.schema import ForeignKey
from dataclasses import dataclass


@dataclass
class ContainerTravel (db.Model):

    data_criacao: Date
    ultima_atualizacao: Date
    
    __tablename__ = 'container_viagem'

    id_container_viagem = Column(Integer, primary_key=True)
    data_criacao = Column(Date, nullable=False)
    ultima_atualizacao = Column(Date, nullable=False)
    id_container = Column(Integer, ForeignKey('containers.id_container', ondelete='cascade'))
    id_viagem = Column(Integer, ForeignKey('viagens.id_viagem', ondelete='cascade'))

