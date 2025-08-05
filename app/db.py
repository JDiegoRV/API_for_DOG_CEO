from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = "DOGS_api_DB"
COLLECTION_NAME = "dog_requests"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def save_dog_request(breed: str, image_url: str, status_code: int):
    dog_data = {
        "breed": breed,
        "image_url": image_url,
        "timestamp": datetime.utcnow(),
        "status_code": status_code
    }
    collection.insert_one(dog_data)

def get_top_breeds(limit: int = 10):
    pipeline = [
    {"$match": {"breed": {"$ne": "test_breed"}}},  
    {"$group": {"_id": "$breed", "requests": {"$sum": 1}}},
    {"$sort": {"requests": -1}},
    {"$limit": limit},
    {"$project": {"_id": 0, "breed": "$_id", "requests": 1}}
]
    return list(collection.aggregate(pipeline))
