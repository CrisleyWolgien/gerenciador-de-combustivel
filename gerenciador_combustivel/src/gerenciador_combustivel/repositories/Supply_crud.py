from sqlmodel import Session
from models.supply import Supply
from models.vehicle import Vehicle
from models.user import Users
from schemas.schemas_supply import createSupply
from uuid import UUID
from fastapi import HTTPException



def create_supply(session: Session, supply: createSupply, user_id: UUID, vehicle_id: UUID) -> Supply:
    vehicle = session.get(Vehicle, vehicle_id)
    if not vehicle:
        if not vehicle:
            raise HTTPException(status_code=404, detail="veiculo não encontrado")
        
    user = session.get(Users, user_id)
    if not user:
        if not user:
            raise HTTPException(status_code=404, detail="Usuario não encontrado")
    supply_data = supply.model_dump()

    if vehicle.id is None:
        raise HTTPException(status_code=400, detail="ID do veiculo está ausente")
    
    session_supply = Supply(
        **supply_data,
        vehicle_id=vehicle_id,
        user_id=user_id,
    )

    session.add(session_supply)
    session.commit()
    session.refresh(session_supply)
    return session_supply
    
