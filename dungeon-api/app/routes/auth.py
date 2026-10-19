from fastapi import FastAPI, APIRouter, HTTPException, Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field
from enum import Enum
from app.models import accounts
from app.database import *
import uuid
import jwt
from pwdlib import PasswordHash

pwd = PasswordHash.recommended()

router = APIRouter(prefix="/auth", tags=["Authentification"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class RegisterModel(BaseModel):
    name: str
    password: str

@router.post("/register")
def a(rm:RegisterModel,session: Session = Depends(get_session)):
    a = accounts.Account()
    a.name = rm.name
    a.pwd = pwd.hash(rm.password)
    session.add(a)
    session.commit()
    session.refresh(a)
    return {"account" : "created"}


code = "c818166b7a9"
@router.post("/login")
def b(form: Annotated[OAuth2PasswordRequestForm, Depends()],session: Session = Depends(get_session)):
    for i in session.query(accounts.Account).all():
        if i.name == form.username:
            if pwd.verify(form.password,i.pwd):
                encode = {"id" : i.id}
                tokan = jwt.encode(encode, code, algorithm="HS256")
                return tokan
            else : 
                raise HTTPException(status_code=401,detail="non authorisé, mauvais mot de passe")
    raise HTTPException(status_code=401,detail="non authorisé, aucun utilisateur avec ce nom")

def check_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, code, algorithms=["HS256"])
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Token invalide")
    return payload["id"]