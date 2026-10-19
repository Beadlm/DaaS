from enum import Enum

from sqlalchemy import Column, Integer, String
from sqlmodel import SQLModel, Field

class Hero(SQLModel,table=True) :
    __tablename__ = "Heros"
    id: int | None = Field(default=None, primary_key=True)

    salle : str #salle_actuelle sur la consigne

    nom :str
    classe : str

    force : int
    agilite : int
    intelligence : int

    pv : int
    pv_max : int

    or_ : int = 0

    monstre_pv : int | None

    victoire : bool = False 

    owner_id : int | None #pour l'instant avant palier 4





