from fastapi import APIRouter, Depends
from sqlmodel import Session

from ..core.db import get_session
from ..core.security import get_current_user
from ..models.user import Users
from ..schemas.schemas_vehicle import CreateVehicle
from ..repositories import vehicle_crud

router = APIRouter (prefix="/vehicle", tags=["vehicle"])

@router.post("/", status_code=201)
def create_vehicle( vehicle_in: CreateVehicle, session: Session = Depends(get_session), current_user: Users = Depends(get_current_user) ):
    if current_user.id is None:
        raise ValueError ("Authenticated user does not have a valid ID")
    vehicle_crud.create_vehicle(session, vehicle_in=vehicle_in)
    return {"Usuario": current_user.name, "vehicle": vehicle_in.name}

@router.get("/", response_model=list[CreateVehicle])
def get_vehicle (session: Session= Depends(get_session)):
    return vehicle_crud.get_vehicle(session)