from sqlalchemy import Column, String, Integer
from dataclasses import dataclass

from app.configs.database import db


@dataclass
class User(db.Model):

    name: str
    username: str

    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False, unique=True)
    password = Column(String(127), nullable=False)
