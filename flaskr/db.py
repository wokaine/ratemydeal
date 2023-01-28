from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

print("Connecting to database...")
try:
    client = MongoClient(
    "mongodb+srv://ratemydeal1:tS0gr4i7Z5sBtos3@cluster0.u1zrqbz.mongodb.net/?retryWrites=true&w=majority", 
    server_api=ServerApi('1'))
    db = client.get_database('meal_deals')
    print("...Connected")
except Exception as e:
    print("Error: ", e)


