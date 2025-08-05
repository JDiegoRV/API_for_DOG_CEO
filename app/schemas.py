from pydantic import BaseModel
#from typing import List

class UserCredentials(BaseModel):
    username: str
    password: str

class DogResponse(BaseModel):
    image_url: str
