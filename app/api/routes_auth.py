from fastapi import APIRouter
from pydantic import BaseModel
from app.core.security import create_token


Router = APIRouter()

class AuthInput(BaseModel):
    username: str
    password: str

@Router.post('/login')
def login(auth: AuthInput):
    if(auth.username=='admin') and (auth.password=='admin'):
        token=create_token({'sub':auth.username})
        return {'acces_token': token}
    
    return {'error':'Invalid Credentials'}