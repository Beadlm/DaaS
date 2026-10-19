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

        he.pv_max = 20 + h.force * 2
        he.pv = he.pv_max

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
with open(dir) as data:
    json_dat = json.load(data)

@router.get("/{hero_id}/room")
def SeeRoom(hero_id : int,session: Session = Depends(get_session)):
    res = session.query(hero.Hero).get(hero_id)
    if res == None:
        raise HTTPException(status_code=404,detail=f"Héro avec ID={hero_id} non trouvé" )
    return json_dat["rooms"][res.salle]


@router.post("/{hero_id}/move")
def MoveHero(hero_id:int,direction:str,session: Session = Depends(get_session)):
    res = session.query(hero.Hero).get(hero_id)
    
    if res == None:
        raise HTTPException(status_code=404,detail=f"Héro avec ID={hero_id} non trouvé" )
    if direction.lower() not in ["nord","sud","est","ouest"]:
        raise HTTPException(status_code=422,detail=f"direction {direction} N'est pas une direction valide (nord,sud,est,ouest)" )
    if direction.lower() not in json_dat["rooms"][res.salle]["exits"].keys():
        raise HTTPException(status_code=400,detail="NO EXIT")
    if res.monstre_pv > 0 : 
        raise HTTPException(status_code=409,detail="IN COMBAT")
    if res.pv == 0 :
        raise HTTPException(status_code=409,detail="HERO DEAD")
    
    a =  json_dat["rooms"][res.salle]["exits"][direction]
    res.salle = a
    if json_dat["rooms"][res.salle]["monster"] != None:
         res.monstre_pv = json_dat["monsters"][json_dat["rooms"][res.salle]["monster"]]["hp"] #dit au jeu que le joueur est en combat
    else : 
         res.monstre_pv = 0 
    session.commit()
    return a



#palier 3 :
from app.domain import logic
@router.post("/{hero_id}/attack")
def a(hero_id:int,session: Session = Depends(get_session)):       
    res = session.query(hero.Hero).get(hero_id)
    if res == None:
        raise HTTPException(status_code=404,detail=f"Héro avec ID={hero_id} non trouvé")
    if json_dat["rooms"][res.salle]["monster"] == None:
         raise HTTPException(status_code=409,detail=f"NO_MONSTER")
    if res.monstre_pv == 0 : 
             raise HTTPException(status_code=409,detail="NO MONSTER")
    if res.pv == 0 :
         raise HTTPException(status_code=409,detail="HERO DEAD")
    
    a = logic.Guerrier(res) #au cas où
    match res.classe : 
         
        case HeroClasse.GUERRIER :
            a = logic.Guerrier(res)

        case HeroClasse.MAGE : 
            a = logic.Mage(res)

        case HeroClasse.VOLEUR : 
            a = logic.Voleur(res)

    monstre = json_dat["monsters"][json_dat["rooms"][res.salle]["monster"]]

    di = a.calculer_degats()
    crit: bool = res.classe == HeroClasse.VOLEUR and a.count == 0
    ds = a.subir_degats(monstre["attack"])
    res.monstre_pv = res.monstre_pv - di if res.monstre_pv - di >= 0 else 0
    if res.monstre_pv >= 0:
        res.pv = res.pv - ds if res.pv - ds >= 0 else 0

    issue = "monstre_vaincu" if res.monstre_pv == 0 else "heros_mort" if res.pv == 0 else "en_cours"
    org = 0 if issue in ["en_cours", "heros_mort"] else monstre["gold"]
    res.or_ += org
    vic = issue == "monstre_vaincu" and monstre["name"] == "La Liche"
    session.commit()
    return { 
        "degats_infliges": di,
        "critique": crit,
        "degats_subis": ds,
        "pv_heros": res.pv,
        "pv_monstre": res.monstre_pv,
        "issue": issue,
        "or_gagne": org,
        "victoire": vic
        }
        


import asyncio
@router.post("/{hero_id}/rest")
async def b(hero_id:int,session: Session = Depends(get_session)):
    res = session.query(hero.Hero).get(hero_id)
    if res == None:
        raise HTTPException(status_code=404,detail=f"Héro avec ID={hero_id} non trouvé")
    if res.pv == 0 :
        raise HTTPException(status_code=409,detail="HERO DEAD")
    if res.monstre_pv > 0 : 
        raise HTTPException(status_code=409,detail="IN COMBAT")
    await asyncio.sleep(3)
    res.pv = res.pv_max
    session.commit()
    return {"health" : "Healed"}
    