from enum import Enum

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import StaticPool


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


engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(bind=engine)