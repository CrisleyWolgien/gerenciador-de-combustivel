from pydantic import BaseModel

class CreateVehicle(BaseModel):
    name: str