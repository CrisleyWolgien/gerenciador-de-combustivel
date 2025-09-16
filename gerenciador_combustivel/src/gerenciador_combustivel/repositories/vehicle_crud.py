from sqlmodel import Session, select

from ..models.vehicle import Vehicle
from ..schemas.schemas_vehicle import CreateVehicle


def create_vehicle(session: Session, vehicle_in: CreateVehicle):
 vehicle_data = vehicle_in.model_dump()

 session_vehicle = Vehicle(**vehicle_data)

 session.add(session_vehicle)
 session.commit()
 session.refresh(session_vehicle)
 return session_vehicle




def get_vehicle (session: Session):
	return session.exec(select(Vehicle)).all()