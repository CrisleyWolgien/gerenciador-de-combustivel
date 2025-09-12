from models.vehicle import Vehicle
from pydantic import BaseModel
from typing import Optional

class CreateVehicle(BaseModel):
    name: str