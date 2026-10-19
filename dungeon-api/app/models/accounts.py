from sqlalchemy import UniqueConstraint
from sqlmodel import SQLModel, Field

class Account(SQLModel,table=True) :
    __tablename__ = "Accounts"
    __table_args__ = (UniqueConstraint("email"),)
    id: int | None = Field(default=None, primary_key=True)
    name:str 
    pwd:str 