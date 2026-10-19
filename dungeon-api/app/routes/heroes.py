from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel, Field
from enum import Enum
router = APIRouter(prefix="/heroes", tags=["Héros"])

class HeroClasse (str,Enum):
    GUERRIER    = "guerrier"
    MAGE        = "mage"
    VOLEUR      = "voleur"

class HeroModel(BaseModel) :
    salle : str = "entree"
    nom : str = Field(..., min_length=3, max_length=20)
    classe : HeroClasse
    force :  int = Field(...,ge=1,le=8)
    agilite : int = Field(...,ge=1,le=8)
    intelligence : int = Field(...,ge=1,le=8)

@router.post("/heroes",status_code=201)
def a(h : HeroModel):
    if h.force + h.agilite + h.intelligence == 10 :
        pass
    raise HTTPException(status_code=400,detail="élément envoyé invalide")