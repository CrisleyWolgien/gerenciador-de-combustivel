from fastapi import APIRouter, Depends
from sqlmodel import Session
from uuid import UUID

from core.db import get_session
from core.security import get_current_user
from models.user import Users
from schemas.schemas_supply import createSupply, readSupply
from models.supply import Supply
from repositories import Supply_crud

router = APIRouter(prefix="/supply", tags=["Supply"])

@router.post("/", status_code=201)
def create_new_supply(
    supply_in: createSupply,
    vehicle_id: UUID,
    session: Session = Depends(get_session),
    current_user: Users = Depends(get_current_user)
):
    if current_user.id is None:
        raise ValueError("Authenticated user does not have a valid ID.")
    Supply_crud.create_supply(session, supply=supply_in, user_id=current_user.id, vehicle_id=vehicle_id)
    return {"Usuario": get_current_user.name, "veiculo": vehicle_id, "Litros": supply_in.liters, "kilometragem": supply_in.km}