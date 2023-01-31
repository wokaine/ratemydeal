from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

username = os.environ.get("MONGO_USERNAME")
password = os.environ.get("MONGO_PASSWORD")

print("Connecting to database...")
try:
    client = MongoClient(
    f"mongodb+srv://{username}:{password}@cluster0.u1zrqbz.mongodb.net/?retryWrites=true&w=majority", 
    server_api=ServerApi('1'))
    db = client.get_database('meal_deals')
    print("...Connected")
except Exception as e:
    print("Error: ", e)


