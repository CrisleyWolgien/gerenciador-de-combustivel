from fastapi import APIRouter, Depends
from sqlmodel import Session

from ..core.db import get_session
from ..schemas.schemas_user import createUser
from ..services import user_service
from ..core.security import get_current_user
from ..models.user import Users

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", status_code=201)
def route_create_new_user(user_in: createUser, session: Session = Depends(get_session)):
    from core.security import get_password_hash
    hashed_password = get_password_hash(user_in.password)
    new_user = user_service.create_new_user(session=session, user_in=user_in, hashed_password=hashed_password)

    return {"id": new_user.id, "name": new_user.name}

@router.get("/", status_code=201)
def read_me(current_user: Users = Depends(get_current_user)):
    return current_user