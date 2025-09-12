from typing import List, Optional
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel

from gerenciador_combustivel.models.supply import Supply


class Users(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    name: str
    password: str
    role: str = Field(default="operator")  # admin ou operator

    supplies: List["Supply"] = Relationship(back_populates="operador")

