import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db import save_dog_request

client = TestClient(app)

def get_token():
    response = client.post("/login", json={"username": "admin", "password": "admin"})
    assert response.status_code == 200
    return response.json()["access_token"]

def test_dog_breed_success():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/dog/breed/hound", headers=headers)

    assert response.status_code == 200
    json_data = response.json()
    assert "image_url" in json_data
    assert json_data["image_url"].startswith("https://")

def test_save_dog_request():
    try:
        save_dog_request("test_breed", "https://example.com/image.jpg", 200)
    except Exception as e:
        pytest.fail(f"save_dog_request lanzó un error inesperado: {e}")
