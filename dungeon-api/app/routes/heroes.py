from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel, Field
from enum import Enum
from models import hero
router = APIRouter(prefix="/heroes", tags=["Héros"])

class HeroClasse (str,Enum):
    GUERRIER    = "guerrier"
    MAGE        = "mage"
    VOLEUR      = "voleur"

class HeroModel(BaseModel) :
    nom : str = Field(..., min_length=3, max_length=20)
    classe : HeroClasse
    force :  int = Field(...,ge=1,le=8)
    agilite : int = Field(...,ge=1,le=8)
    intelligence : int = Field(...,ge=1,le=8)

@router.post("/heroes",status_code=201)
def a(h : HeroModel):
    with hero.SessionLocal() as session:
        if h.force + h.agilite + h.intelligence == 10 :
            he = hero.Hero()
            he.nom = h.nom
            he.classe = h.classe
            he.force = h.force
            he.agilite = h.agilite
            he.intelligence = h.intelligence
            he.salle = "entree"

            session.add(he)
            session.commit
            session.refresh(he)

            return he
            
        raise HTTPException(status_code=422,detail="élément envoyé invalide")