from sqlmodel import Session
from fastapi import HTTPException

from ..schemas.schemas_user import createUser
from ..repositories.user_crud import get_user_by_name, create_user

def create_new_user(session: Session, user_in: createUser, hashed_password: str):

    existing_user = get_user_by_name(session, user_in.name)
    if existing_user:
        raise HTTPException(status_code=400, detail="Usuário já existe")

    return create_user(session ,user_in, hashed_password)

