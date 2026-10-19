from fastapi import FastAPI, APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from enum import Enum
from app.models import accounts
from app.database import *
import uuid
import jwt
from pwdlib import PasswordHash

pwd = PasswordHash.recommended()

router = APIRouter(prefix="/auth", tags=["Authentification"])


class RegisterModel(BaseModel):
    name: str
    password: str

class LoginModel(BaseModel):
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


@router.post("/login")
def b(lm:RegisterModel,session: Session = Depends(get_session)):
    for i in session.query(accounts.Account).all():
        if i.name == lm.name:
            pass
    raise HTTPException(status_code=401,detail="non authorisé, aucun utilisateur avec ce nom")