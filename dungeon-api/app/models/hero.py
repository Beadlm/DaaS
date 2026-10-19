from enum import Enum

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class HeroClasse(str,Enum):
    GUERRIER    = "guerrier"
    MAGE        = "mage"
    VOLEUR      = "voleur"


class Hero(Base) :
    __tablename__ = "Héros"

    id = Column(Integer, primary_key=True, index=True)
    salle =  Column(String)
    nom = Column(String)
    classe = Column(String)
    force = Column(Integer)
    agilite = Column(Integer)
    intelligence = Column(Integer)


