from fastapi import APIRouter, HTTPException, Depends
from fastapi_jwt_auth import AuthJWT
from app.db import get_top_breeds, save_dog_request
from app.schemas import DogResponse
import httpx

router = APIRouter()

@router.get("/dog/breed/{breed_name}", response_model=DogResponse)
async def get_dog_image(breed_name: str, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or missing JWT token")
    url = f"https://dog.ceo/api/breed/{breed_name}/images/random"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    status_code = response.status_code
    if status_code != 200:
        raise HTTPException(status_code=404, detail="Breed not found or external API error")
    try:
        data = response.json()
    except Exception:
        raise HTTPException(status_code=500, detail="Invalid response from external API")
    if data.get("status") != "success":
        raise HTTPException(status_code=400, detail="Invalid breed or API issue")
    image_url = data["message"]
    save_dog_request(breed_name, image_url, status_code)
    return {
        "image_url": image_url,
    }

@router.get("/dog/stats")
def get_dog_stats(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or missing JWT token")

    top_breeds = get_top_breeds()
    return {"stats": top_breeds}
