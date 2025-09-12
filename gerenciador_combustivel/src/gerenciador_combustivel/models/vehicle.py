from typing import List, Optional
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel

from .supply import Supply


class Vehicle(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    name: str
    
    supplies: List["Supply"] = Relationship(back_populates="vehicle")
    