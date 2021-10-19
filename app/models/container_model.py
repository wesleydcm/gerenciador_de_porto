from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db
from sqlalchemy import Column, Integer, String
from dataclasses import dataclass


@dataclass
class Container(db.Model):

    tracking_code: str
    teu: int
    type: str

    __tablename__ = 'containers'

    id_container = Column(Integer, primary_key=True)
    tracking_code = Column(String, nullable=False, unique=True)
    teu = Column(Integer, nullable=False, default=1)
    type = Column(String(255), nullable=False, default='dry box')
    id_shipping_company = Column(
        Integer, ForeignKey(
            "shipping_company.id_shipping_company", ondelete="cascade"
        )
    )

    travels = relationship('Travel',
                           secondary='container_travel', backref='containers')

    harbors = relationship('Harbor',
                           secondary='container_harbor', backref='containers')
