from typing import List, Optional
from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel

class Supply(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    liters: float
    km: float
    date: str
    user_id: UUID = Field(foreign_key="users.id")
    operador: "Users" = Relationship(back_populates="supplies")  # pyright: ignore[reportUndefinedVariable] # many-to-one  # noqa: F821
    vehicle_id: int = Field(foreign_key="vehicle.id")
    vehicle: Optional["Vehicle"] = Relationship(back_populates="supplies")# pyright: ignore[reportUndefinedVariable] # many-to-one  # noqa: F821
