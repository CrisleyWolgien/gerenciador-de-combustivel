from typing import Optional
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel

from .user import Users 
from .vehicle import Vehicle # Make sure this import path is correct


class Supply(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    liters: float
    km: float
    date: str

    # FK → usuário que fez o abastecimento
    user_id: UUID = Field(foreign_key="users.id")
    vehicle_id: UUID = Field(foreign_key="vehicle.id")

    operador: "Users" = Relationship(back_populates="supplies")
    vehicle: "Vehicle" = Relationship(back_populates="supplies")