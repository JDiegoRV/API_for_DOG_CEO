from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.routes import router as dog_router
from app.auth import auth_router
from app.config import get_config  

app = FastAPI(
    title="API for DOG CEO",
    description="Internal API that connects to the Dog.CEO and stores data",
)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    openapi_schema["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

app.include_router(dog_router)

@app.get("/")
def root():
    return {"message": "Welcome to the API for DOG CEO"}
app.include_router(auth_router)
