from sqlalchemy import Column, Integer, String
from sqlmodel import SQLModel, Field

class Account(SQLModel,table=True) :
    __tablename__ = "Accounts"
    id: int | None = Field(default=None, primary_key=True)
    name:str
    pwd:str