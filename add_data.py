import os
from pymongo import MongoClient
import random
import string

# Use MONGODB_URI or construct from MONGO_PASSWORD
_mongo_uri = os.environ.get("MONGODB_URI")
if not _mongo_uri:
    _password = os.environ.get("MONGO_PASSWORD", "")
    _mongo_uri = f"mongodb+srv://player:{_password}@cluster0.oe6qr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" if _password else "placeholder"
client = MongoClient(_mongo_uri)

db = client['car_unlock_system']  
collection = db['users']

#Token Generation
characters = string.ascii_letters + string.digits  # Includes uppercase, lowercase, and digits
token = ''.join(random.choice(characters) for _ in range(16))

user_id=input("Enter User ID: ")
car_id=input("Enter Car ID: ")
new_data = {
    "user_id":user_id,
    "car_id":car_id,    
    "token":token,
}

# Insert the data into the collection
result = collection.insert_one(new_data)

# Print a confirmation
print(f"Data inserted with ID: {result.inserted_id}")
