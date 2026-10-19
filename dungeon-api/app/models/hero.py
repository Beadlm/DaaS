from sqlmodel import SQLModel, Field

class Hero(SQLModel, table=True) :
    __tablename__ = "Héros"

    id : int | None = Field(default=0, primary_key=True)
    salle : str = "entree"

    nom : str = Field(..., min_length=3, max_length=20)
    classe : str
    force : int
    agilite : int
    intelligence : int


