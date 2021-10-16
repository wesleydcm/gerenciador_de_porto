from sqlalchemy import Column, String, Integer
from dataclasses import dataclass
from werkzeug.security import check_password_hash, generate_password_hash

from app.configs.database import db


@dataclass
class User(db.Model):
    id_user: int
    name: str
    username: str

    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(512), nullable=False)

    @property
    def password(self):
        raise AttributeError("Password is not acessible")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def check_password(self, password_to_hash):
        is_valid = check_password_hash(self.password_hash, password_to_hash)
        return is_valid
