from pydantic import BaseModel
from datetime import date

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

class SupplyFilter(BaseModel):
    start_date: date
    end_date: date