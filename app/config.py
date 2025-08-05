import os
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseModel):
    authjwt_secret_key: str = os.getenv("JWT_SECRET", "clave123") 
    authjwt_algorithm: str = "HS256"

from fastapi_jwt_auth import AuthJWT
@AuthJWT.load_config
def get_config():
    return Settings()
