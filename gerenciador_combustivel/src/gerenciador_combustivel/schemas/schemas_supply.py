from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class createSupply(BaseModel):
    liters: float
    km: float
    date: str

class readSupply(BaseModel):
    id: int
    liters: float
    km: float
    date: str

    class Config:
        orm_mode = True

