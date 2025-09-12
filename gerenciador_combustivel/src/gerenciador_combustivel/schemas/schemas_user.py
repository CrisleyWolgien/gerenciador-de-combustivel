from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class createUser(BaseModel):
    name: str
    password: str
    role: str

class updateUser(BaseModel):
    name: Optional[str]
    password: Optional[str]
    role: Optional[str]

class loginUser(BaseModel):
    name: str
    password: str

class userRead(BaseModel):
    id: UUID
    name: str
    role: str
    
    class Config:
        orm_mode = True

