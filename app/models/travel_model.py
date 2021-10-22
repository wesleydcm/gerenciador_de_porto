from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey


@dataclass
class Travel(db.Model):

    destination: str
    code: str

    __tablename__ = "travel"

    id_travel = Column(Integer, primary_key=True)
<<<<<<< HEAD
    travel_code = Column(String(127), nullable=True, unique=True)
    destination = Column(String(63), nullable=False)
=======
    destination = Column(String, nullable=False, unique=True)
    code = Column(Integer, nullable=False, unique=True)
>>>>>>> 78197d889ca7011c0075934cf323d8c0d2cd9b7d
    id_ship = Column(
        Integer, ForeignKey("ships.id_ship", ondelete="cascade")
    )
