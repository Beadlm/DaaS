from enum import Enum

from sqlalchemy import Column, Integer, String
from sqlmodel import SQLModel, Field

class Hero(SQLModel,table=True) :
    __tablename__ = "Heros"
    id: int | None = Field(default=None, primary_key=True)
    salle : str
    nom :str
    classe : str
    force : int
    agilite : int
    intelligence : int


