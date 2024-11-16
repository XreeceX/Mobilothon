# app.py
from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

password = os.environ["MONGO_PASSWORD"]
# Connect to MongoDB
client = MongoClient(f"mongodb+srv://player:{password}@cluster0.oe6qr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.car_unlock_system
users_collection = db['users']

# Helper function to check if the user exists
def user_exists(user_id, car_id,token):
    user = users_collection.find_one({"user_id": user_id, "car_id": car_id, "token": token})
    return user

# Endpoint to unlock the car
@app.route('/unlock', methods=['POST'])
def unlock_car():
    data = request.get_json()
    user_id = data.get('user_id')
    car_id = data.get('car_id')
    token=data.get('token')
    
    # Check if the user exists
    user = user_exists(user_id, car_id,token)
    
    if user:
        return jsonify({"message": "Car unlocked successfully!"}), 200
    else:
        return jsonify({"message": "User not found or not authorized."}), 403

# Endpoint to lock the car
@app.route('/lock', methods=['POST'])
def lock_car():
    data = request.get_json()
    user_id = data.get('user_id')
    car_id = data.get('car_id')
    token=data.get('token')
    
    # Check if the user exists
    user = user_exists(user_id, car_id,token)
    
    if user:
        return jsonify({"message": "Car locked successfully!"}), 200
    else:
        return jsonify({"message": "User not found or not authorized."}), 403

if __name__ == '__main__':
    app.run(debug=True)
