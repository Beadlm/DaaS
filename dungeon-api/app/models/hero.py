from enum import Enum
from sqlmodel import SQLModel, Field
class HeroClasse (str,Enum):
    GUERRIER    = "guerrier"
    MAGE        = "mage"
    VOLEUR      = "voleur"

class Hero(SQLModel, table=True) :
    __tablename__ = "Héros"

    id : int | None = Field(default=0, primary_key=True)
    salle : str = "entree"

    nom : str = Field(..., min_length=3, max_length=20)
    classe : HeroClasse
    force : int
    agilite : int
    intelligence : int


