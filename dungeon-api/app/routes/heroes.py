from fastapi import FastAPI, APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from enum import Enum
from app.models import hero
from app.database import *
import json

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

@router.post("",status_code=201)
def addHero(h : HeroModel, session: Session = Depends(get_session)):
    if h.force + h.agilite + h.intelligence == 10 : #je peux pas faire ça sur pydantic si?
        he = hero.Hero()
        he.nom = h.nom
        he.classe = h.classe
        he.force = h.force
        he.agilite = h.agilite
        he.intelligence = h.intelligence
        he.salle = "entree"

        session.add(he)
        session.commit()
        session.refresh(he)

        return he
        
    raise HTTPException(status_code=422,detail="élément envoyé invalide")


@router.get("")
def getAllHeroes(session: Session = Depends(get_session)):
        return session.query(hero.Hero).all()


@router.get("/{hero_id}")
def getHero(hero_id : int,session: Session = Depends(get_session)):
        res = session.query(hero.Hero).get(hero_id)
        if res == None:
            raise HTTPException(status_code=404,detail=f"Héro avec ID={hero_id} non trouvé" )
        return res


#palier 2
from pathlib import Path
dir = Path(__file__).resolve().parent.parent.parent / "data" / "dungeon_map.json"
@router.get("/{hero_id}/room")
def a(hero_id : int,session: Session = Depends(get_session)):
    res = session.query(hero.Hero).get(hero_id)
    if res == None:
        raise HTTPException(status_code=404,detail=f"Héro avec ID={hero_id} non trouvé" )
    with open(dir) as data:

         a = json.load(data)
    return a["rooms"][res.salle]