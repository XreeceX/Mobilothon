from pymongo import MongoClient
import random,string
import os

password = os.environ["MONGO_PASSWORD"]

# Replace this with your MongoDB connection string
client = MongoClient(f"mongodb+srv://player:{password}@cluster0.oe6qr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

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
