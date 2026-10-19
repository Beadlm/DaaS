from fastapi import FastAPI, APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from enum import Enum
from app.models import accounts
from app.database import *
import bcrypt
import uuid
from passlib.context import CryptContext
from jose import jwt


pwd = CryptContext(schemes=["pbkdf2_sha256"])

router = APIRouter(prefix="/auth", tags=["Authentification"])


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
