from enum import Enum

from sqlalchemy import Column, Integer, String
from sqlmodel import SQLModel


class HeroClasse(str,Enum):
    GUERRIER    = "guerrier"
    MAGE        = "mage"
    VOLEUR      = "voleur"


class Hero(SQLModel,table=True) :
    __tablename__ = "Heros"

    id = Column(Integer, primary_key=True, index=True)
    salle =  Column(String)
    nom = Column(String)
    classe = Column(String)
    force = Column(Integer)
    agilite = Column(Integer)
    intelligence = Column(Integer)


