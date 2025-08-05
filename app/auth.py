from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from app.schemas import UserCredentials


auth_router = APIRouter()

@auth_router.post("/login")
def login(credentials: UserCredentials, Authorize: AuthJWT = Depends()):
    if credentials.username != "admin" or credentials.password != "admin":
        raise HTTPException(status_code=401, detail="Bad username or password")

    access_token = Authorize.create_access_token(subject=credentials.username)
    return {"access_token": access_token}