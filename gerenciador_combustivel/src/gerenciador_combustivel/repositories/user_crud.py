from sqlmodel import Session, select

from ..models.user import Users
from ..schemas.schemas_user import createUser

def create_user(session: Session, user_in: createUser, hashed_password: str) -> Users:

    user_data = user_in.model_dump()
    user_data.pop("password")

    session_user= Users(**user_data, password=hashed_password)

    session.add (session_user)
    session.commit()
    session.refresh(session_user)

    return session_user

def get_user_by_name(session: Session, name: str) -> Users | None:
    return session.exec(select(Users).where(Users.name == name)).first()